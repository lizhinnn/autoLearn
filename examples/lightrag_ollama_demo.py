import os
import logging
from lightrag import LightRAG, QueryParam
from lightrag.llm import ollama_model_complete, ollama_embedding
from lightrag.utils import EmbeddingFunc
from lightrag.translate import translate2zh
# from lightrag.image import process_images_with_llama
from datetime import datetime

now = datetime.now()
formatted_time = now.strftime("%m%d")

WORKING_DIR = f"./automationMDOllama_TEXT0112"

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=ollama_model_complete,
    llm_model_name="llama3.1:8b",
    llm_model_max_async=4,
    llm_model_max_token_size=32768,
    # llm_model_kwargs={"host": "http://localhost:11434", "options": {"num_ctx": 32768}},
    llm_model_kwargs={
        "host": "http://localhost:11434",
        "options": {
            "num_ctx": 32768,
            # "num_gpu": 1,  # 指定使用GPU数量
            # "numa": True,  # 启用NUMA优化
        }
    },
    embedding_func=EmbeddingFunc(
        embedding_dim=768,
        max_token_size=8192,
        func=lambda texts: ollama_embedding(
            texts, embed_model="nomic-embed-text:latest", host="http://localhost:11434"
        ),
    ),
)




# import glob
# from PIL import Image
# from transformers import CLIPProcessor, CLIPModel

# def process_images_in_directory(directory_path):
#     # 初始化CLIP模型和处理器
#     model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
#     processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

#     # 获取目录下所有图片文件
#     image_files = glob.glob(os.path.join(directory_path, "*.jpg")) + glob.glob(os.path.join(directory_path, "*.png"))

#     # 处理每张图片
#     for image_file in image_files:
#         image = Image.open(image_file)
#         inputs = processor(images=image, return_tensors="pt")
#         outputs = model.get_text_features(**inputs)
#         text_representation = outputs[0].cpu().detach().numpy()
#         print(f"Image: {image_file}, Text Representation: {text_representation}")

# # 调用函数处理image目录下的所有图片
# process_images_in_directory("image")




# #处理单个markdown文件
# def process_markdown_file(file_path):
#     with open(file_path,"r",encoding="utf-8")as f:
#         return f.read()
    
# #处理markdown文件
# markdown_file = "./Markdown.md"#替换为你的markdown文件路径
# # 调用函数处理图片
# process_images_with_llama(
#     "Markdown.md",  # 更新为Markdown.md文件路径
#     max_workers=2
# )
# markdown_content = process_markdown_file(markdown_file)
# rag.insert(markdown_content)


#如果需要处理多个markdown文件,可以使用以下代码
# def process_markdown_directory (directory):
#     markdown_contents =[]
#     for filename in os.listdir(directory):
#           if fiLename.endswith('.md '):

# pdf文件导入
# from pypdf import PdfReader

# file_path = 'pdfTest.pdf'
# reader = PdfReader(file_path)
# text_content = ""
# for page in reader.pages:
#     text_content += page.extract_text()

# rag.insert(text_content)
# ... existing code ...
#------------------------------------------------------------------------------------


# txt文件导入
# with open("./book.txt", "r", encoding="utf-8") as f:
#     rag.insert(f.read())


#------------------------------------------------------------------------------------

# queryQuestion = "what is Open-Loop Control ?"

# print("question:",queryQuestion)

# # Perform naive search
# # print("query mode : naive")
# # nativeAnswer = rag.query(queryQuestion, param=QueryParam(mode="naive"))
# with open(f"{WORKING_DIR}/naive{formatted_time}.md", "w", encoding="utf-8") as f:
#     f.write(f"TEXT TIME : {now}\n")
#     f.write("query mode : naive\n")
#     f.write(rag.query(queryQuestion, param=QueryParam(mode="naive")))

# # Perform local search
# # print("query mode : local")
# # localAnswer = rag.query(queryQuestion, param=QueryParam(mode="local"))
# with open(f"{WORKING_DIR}/local{formatted_time}.md", "w", encoding="utf-8") as f:
#     f.write(f"TEXT TIME : {now}\n")
#     f.write("query mode : local\n")
#     f.write(rag.query(queryQuestion, param=QueryParam(mode="local")))

# # Perform global search
# # print("query mode : global")
# # globalAnswer = rag.query(queryQuestion, param=QueryParam(mode="global"))
# with open(f"{WORKING_DIR}/global{formatted_time}.md", "w", encoding="utf-8") as f:
#     f.write(f"TEXT TIME : {now}\n")
#     f.write("query mode : global\n")
#     f.write(rag.query(queryQuestion, param=QueryParam(mode="global")))

# # Perform hybrid search
# # print("query mode : hybrid")
# # hybridAnswer = rag.query(queryQuestion, param=QueryParam(mode="hybrid"))
# with open(f"{WORKING_DIR}/hybrid{formatted_time}.md", "w", encoding="utf-8") as f:
#     f.write(f"TEXT TIME : {now}\n")
#     f.write("query mode : hybrid\n")
#     f.write(rag.query(queryQuestion, param=QueryParam(mode="hybrid")))


#---------------------------------------------------------------------------------------

questionBank_path = r"C:\Users\Dyson\LightRAG\questionBank\gather.md"

# 使用 with 语句打开文件并读取内容
try:
    with open(questionBank_path, "r", encoding="utf-8") as file:
        content = file.read()
        # 按 ## 分割问题，并去除空字符串
        questions = [q.strip() for q in content.split('##') if q.strip()]
        
        # 为每个问题创建一个目录
        question_dir = os.path.join(WORKING_DIR, "questions")
        if not os.path.exists(question_dir):
            os.makedirs(question_dir)
        
        # 处理每个问题
        for i, question in enumerate(questions, 1):
            print(f"Processing question {i}/{len(questions)}")
            
            # 为当前问题创建一个子目录
            current_question_dir = os.path.join(question_dir, f"question_{i}")
            if not os.path.exists(current_question_dir):
                os.makedirs(current_question_dir)
            
            # 获取问题的第一行作为标题
            question_title = question.split('\n')[0].strip()
            
            # 对每个问题进行不同模式的查询
            modes = ["naive", "local", "global", "hybrid"]
            for mode in modes:
                # 普通查询
                response = rag.query(
                    question,
                    param=QueryParam(mode=mode)
                )
                
                file_path = os.path.join(current_question_dir, f"{mode}_{formatted_time}.md")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"# Question {i}: {question_title}\n\n")
                    f.write(f"Query Time: {now}\n")
                    f.write(f"Query Mode: {mode}\n\n")
                    f.write("## Original Question\n")
                    f.write(question + "\n\n")
                    f.write("## Answer\n")
                    f.write(response)
                
                # 启用思维链的查询
                cot_response = rag.query(
                    question,
                    param=QueryParam(mode=mode, enable_cot=True)
                )
                
                cot_file_path = os.path.join(current_question_dir, f"COT_{mode}_{formatted_time}.md")
                with open(cot_file_path, "w", encoding="utf-8") as f:
                    f.write(f"# Question {i}: {question_title}\n\n")
                    f.write(f"Query Time: {now}\n")
                    f.write(f"Query Mode: {mode} with chain of thought\n\n")
                    f.write("## Original Question\n")
                    f.write(question + "\n\n")
                    f.write("## Answer (with Chain of Thought)\n")
                    f.write(cot_response)
            
            print(f"Completed question {i}")
        
        print("All questions processed successfully")

except FileNotFoundError:
    print(f"Error: 文件 '{questionBank_path}' 未找到，请检查路径是否正确。")
except Exception as e:
    print(f"Error: 发生未知错误 - {e}")
    import traceback
    traceback.print_exc()