import os
import glob
from PIL import Image
import base64
from io import BytesIO
import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import re  # 导入正则表达式模块

def encode_image_to_base64(image_path):
    """将图片转换为base64编码"""
    with Image.open(image_path) as image:
        buffered = BytesIO()
        image.save(buffered, format=image.format)
        return base64.b64encode(buffered.getvalue()).decode('utf-8')

def create_retry_session(retries=3, backoff_factor=0.5, timeout=60):
    """创建带有重试机制的session"""
    session = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def process_image_batch(image_files, batch_size=8):
    """批量处理图片"""
    results = []
    session = create_retry_session()  # 创建带重试的session
    
    # output_file = "image_descriptions.txt"  # 定义输出文件路径
    
    for image_file in image_files:
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                base64_image = encode_image_to_base64(image_file)
                
                data = {
                    "model": "llama3.2-vision:latest",
                    "prompt": "Describe the picture in detail",
                    "images": [base64_image],
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "top_p": 0.9,
                        "num_predict": 10000
                    }
                }
                
                print(f"正在处理图片 (尝试 {attempt + 1}/{max_attempts}): {image_file}")
                response = session.post(
                    'http://localhost:11434/api/generate', 
                    json=data,
                    headers={'Content-Type': 'application/json'},
                    timeout=600  # 增加超时时间到60秒
                )
                
                print(f"API响应状态码: {response.status_code}")
                
                if response.status_code == 200:
                    result = response.json()
                    description = result.get('response', '无法获取描述')
                    results.append((image_file, description))
                    print(f"成功处理图片: {image_file}")
                    
                    # # 直接写入输出文件
                    # with open(output_file, "a", encoding="utf-8") as f:
                    #     f.write(f"image: {image_file}\n")
                    #     f.write(f"description: {description}\n")
                    #     f.write("-" * 50 + "\n")
                    
                    # 替换Markdown.md中的图片路径为描述
                    replace_image_path_in_markdown("Markdown.md", image_file, description)
                    
                    break  # 成功后跳出重试循环
                else:
                    error_msg = f"处理失败: API状态码 {response.status_code}, 响应: {response.text[:100]}"
                    print(error_msg)
                    if attempt == max_attempts - 1:  # 最后一次尝试失败
                        results.append((image_file, error_msg))
                        
            except Exception as e:
                error_msg = f"处理错误: {str(e)}"
                print(f"{error_msg} (尝试 {attempt + 1}/{max_attempts})")
                if attempt == max_attempts - 1:  # 最后一次尝试失败
                    results.append((image_file, error_msg))
                else:
                    time.sleep(2 ** attempt)  # 指数退避
    
    return results

def get_existing_descriptions(output_file):
    """获取已经处理过的图片列表"""
    processed_images = set()
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # 使用文件路径作为标识
            for line in content.split('\n'):
                if line.startswith('图片: '):
                    processed_images.add(line[4:].strip())
    return processed_images

def get_image_paths_from_markdown(markdown_file):
    """从Markdown文件中提取图片路径"""
    image_paths = []
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
        # 使用正则表达式匹配图片路径
        image_paths = re.findall(r'!\[\]\((.*?)\)', content)
    return image_paths

def process_images_with_llama(markdown_file, max_workers=2):
    """并行处理多张图片"""
    # 从Markdown文件中获取图片路径
    image_files = get_image_paths_from_markdown(markdown_file)
    print(f"找到的图片数量: {len(image_files)}")
    
    output_file = "image_descriptions.txt"
    
    # 获取已处理的图片列表
    processed_images = get_existing_descriptions(output_file)
    print(f"已处理的图片数量: {len(processed_images)}")
    
    # 过滤出未处理的图片
    new_image_files = [f for f in image_files if f not in processed_images]
    print(f"新图片数量: {len(new_image_files)}")
    
    if not new_image_files:
        print("没有新的图片需要处理！")
        return
    
    # 将新图片列表分成多个小批次
    batch_size = len(new_image_files) // max_workers
    if batch_size == 0:
        batch_size = 1
    batches = [new_image_files[i:i + batch_size] for i in range(0, len(new_image_files), batch_size)]
    
    # 使用线程池并行处理图片批次
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_batch = {
            executor.submit(process_image_batch, batch): batch
            for batch in batches
        }
        
        # 收集结果
        all_results = []
        for future in as_completed(future_to_batch):
            try:
                batch_results = future.result()
                all_results.extend(batch_results)
                print(f"已完成一批图片处理")
            except Exception as e:
                print(f"处理批次时出错: {str(e)}")
    
    print(f"所有图片处理完成！描述已保存到 {output_file}")

def replace_image_path_in_markdown(markdown_file, image_file, description):
    """替换Markdown文件中的图片路径为描述"""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换图片路径为描述
    # new_content = content.replace(f"![]({image_file})\nFigure", description)
    new_content = content.replace(f"![]({image_file})  \nFigure", description)
    
    with open(markdown_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

# 调用函数处理图片
process_images_with_llama(
    "Markdown.md",  # 更新为Markdown.md文件路径
    max_workers=2
)
