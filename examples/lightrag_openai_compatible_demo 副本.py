import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio
from lightrag import LightRAG, QueryParam
from lightrag.llm import openai_complete_if_cache, openai_embedding
from lightrag.llm import ollama_model_complete, ollama_embedding
from lightrag.utils import EmbeddingFunc
# from lightrag.image import process_images_with_llama
import numpy as np
from datetime import datetime

now = datetime.now()
formatted_time = now.strftime("%m%d")


WORKING_DIR = "./aNofigure0209"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

# 在文件开头添加 API key 设置
os.environ["OPENAI_API_KEY"] = "sk-HTOktt1iYGmU9ZNIdtiSs8XpNM3YCy3tNZFGqa8jvi5HI9w1"  # 替换为你的实际 API key

async def llm_model_func(
    prompt, system_prompt=None, history_messages=[], **kwargs
) -> str:
    return await openai_complete_if_cache(
        "gpt-4o-2024-08-06",
        # "solar-mini",
        prompt,
        system_prompt=system_prompt,
        history_messages=history_messages,
        # api_key=os.getenv("sk-HTOktt1iYGmU9ZNIdtiSs8XpNM3YCy3tNZFGqa8jvi5HI9w1"),
        # api_key=os.getenv("UPSTAGE_API_KEY"),
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://pro.xiaoai.plus/v1",
        # base_url="https://api.upstage.ai/v1/solar",
        **kwargs,
    )

# async def embedding_func(texts:list[str]) -> np.ndarray:
#     return await ollama_embedding(
#         texts,
#         embed_model="nomic-embed-text",
#     )

async def embedding_func(texts: list[str]) -> np.ndarray:
    return await openai_embedding(
        texts,
        model="text-embedding-3-small",
        # model="solar-embedding-1-large-query",
        # api_key=os.getenv("sk-HTOktt1iYGmU9ZNIdtiSs8XpNM3YCy3tNZFGqa8jvi5HI9w1"),
        # api_key=os.getenv("UPSTAGE_API_KEY"),
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://pro.xiaoai.plus/v1",
        # base_url="https://api.upstage.ai/v1/solar",
    )


async def get_embedding_dim():
    test_text = ["This is a test sentence."]
    embedding = await embedding_func(test_text)
    embedding_dim = embedding.shape[1]
    return embedding_dim


# function test
async def test_funcs():
    result = await llm_model_func("How are you?")
    print("llm_model_func: ", result)

    result = await embedding_func(["How are you?"])
    print("embedding_func: ", result)


# asyncio.run(test_funcs())

#处理单个markdown文件
def process_markdown_file(file_path):
    with open(file_path,"r",encoding="utf-8")as f:
        return f.read()
    


async def main():
    try:
        embedding_dimension = await get_embedding_dim()
        print(f"Detected embedding dimension: {embedding_dimension}")

        rag = LightRAG(
            working_dir=WORKING_DIR,
            llm_model_func=llm_model_func,
            embedding_func=EmbeddingFunc(
                # embedding_dim=768,
                embedding_dim=embedding_dimension,
                max_token_size=8192,
                func=embedding_func,
            ),
        )


        # 图转文
        # process_images_with_llama(
        #     r"C:\Users\Dyson\LightRAGDemo\images",
        #     max_workers=2
        # )



        #处理markdown文件
        # markdown_file = "./Markdown_nofigure.md"#替换为你的markdown文件路径
        # markdown_content = process_markdown_file(markdown_file)
        # await rag.ainsert(markdown_content)


        # # pdf文件导入
        # from pypdf import PdfReader

        # file_path = 'pdfTest.pdf'
        # reader = PdfReader(file_path)
        # text_content = ""
        # for page in reader.pages:
        #     text_content += page.extract_text()

        # await rag.ainsert(text_content)  



        # with open("./book.txt", "r", encoding="utf-8") as f:
        #     await rag.ainsert(f.read())

        questionBank_path = r"C:\Users\Dyson\LightRAG\questionBank\gather.md"
        # 或者使用正斜杠: "C:/Users/Dyson/LightRAG/questionBank/gather.md"

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
                        response = await rag.aquery(
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
                        cot_response = await rag.aquery(
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
        


        # queryQuestion = 'What is the root locus? Plot the root locus of\
        #       the system step by step according to the principle and steps of\
        #           tracing root locus: $G(s)H(s)=\\frac{K^*}{s^4+4s^3+12s^2+20s+10}$Tracing \
        #             root locus, please give the specific analysis method of each step,matlab code is also given.'

        # Perform naive search
        # print("query mode : naive")
        # print(
        #     await rag.aquery(
        #         queryQuestion, param=QueryParam(mode="naive")
        #     )
        # )
        
        # 启用思维链的查询
        with open(f"{WORKING_DIR}/COT_naive{formatted_time}.md", "w", encoding="utf-8") as f:
            f.write(f"TEXT TIME : {now}\n")
            f.write("query mode : naive with chain of thought\n")
            f.write(await rag.aquery(
                queryQuestion, 
                param=QueryParam(mode="naive", enable_cot=True)
            ))

        with open(f"{WORKING_DIR}/COT_local{formatted_time}.md", "w", encoding="utf-8") as f:
            f.write(f"TEXT TIME : {now}\n")
            f.write("query mode : local with chain of thought\n")
            f.write(await rag.aquery(
                queryQuestion,
                param=QueryParam(mode="local", enable_cot=True)
            ))        

        with open(f"{WORKING_DIR}/COT_global{formatted_time}.md", "w", encoding="utf-8") as f:
            f.write(f"TEXT TIME : {now}\n")
            f.write("query mode : global with chain of thought\n")
            f.write(await rag.aquery(
                queryQuestion, 
                param=QueryParam(mode="global", enable_cot=True)
            ))
            
        
        with open(f"{WORKING_DIR}/COT_hybrid{formatted_time}.md", "w", encoding="utf-8") as f:
            f.write(f"TEXT TIME : {now}\n")
            f.write("query mode : hybrid with chain of thought\n")
            f.write(await rag.aquery(
                queryQuestion,
                param=QueryParam(mode="hybrid", enable_cot=True)
            ))


        with open(f"{WORKING_DIR}/naive{formatted_time}.md", "w", encoding="utf-8") as f:
            f.write(f"TEXT TIME : {now}\n")
            f.write("query mode : naive\n")
            f.write(await rag.aquery(queryQuestion, param=QueryParam(mode="naive")))  

        # Perform local search
        # print("query mode : local")
        # print(
        #     await rag.aquery(
        #         queryQuestion, param=QueryParam(mode="local")
        #     )
        # )

        with open(f"{WORKING_DIR}/local{formatted_time}.md", "w", encoding="utf-8") as f:
            f.write(f"TEXT TIME : {now}\n")
            f.write("query mode : local\n")
            f.write(await rag.aquery(queryQuestion, param=QueryParam(mode="local")))    

        # Perform global search
        # print("query mode : global")
        # print(
        #     await rag.aquery(
        #         queryQuestion,
        #         param=QueryParam(mode="global"),
        #     )
        # )


        with open(f"{WORKING_DIR}/global{formatted_time}.md", "w", encoding="utf-8") as f:
            f.write(f"TEXT TIME : {now}\n")
            f.write("query mode : global\n")
            f.write(await rag.aquery(queryQuestion, param=QueryParam(mode="global")))

        # Perform hybrid search
        # print("query mode : hybrid")
        # print(
        #     await rag.aquery(
        #         queryQuestion,
        #         param=QueryParam(mode="hybrid"),
        #     )
        # )

        with open(f"{WORKING_DIR}/hybrid{formatted_time}.md", "w", encoding="utf-8") as f:
            f.write(f"TEXT TIME : {now}\n")
            f.write("query mode : hybrid\n")
            f.write(await rag.aquery(queryQuestion, param=QueryParam(mode="hybrid")))

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()  # 打印完整的错误堆栈


if __name__ == "__main__":
    asyncio.run(main())
