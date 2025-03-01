import os
import asyncio
from lightrag import LightRAG, QueryParam
from lightrag.llm import openai_complete_if_cache, openai_embedding
from lightrag.llm import ollama_model_complete, ollama_embedding
from lightrag.utils import EmbeddingFunc
import numpy as np

WORKING_DIR = "./automationMarkdown"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)


async def llm_model_func(
    prompt, system_prompt=None, history_messages=[], **kwargs
) -> str:
    return await openai_complete_if_cache(
        "gpt-4o-2024-08-06",
        # "solar-mini",
        prompt,
        system_prompt=system_prompt,
        history_messages=history_messages,
        api_key=os.getenv("sk-HTOktt1iYGmU9ZNIdtiSs8XpNM3YCy3tNZFGqa8jvi5HI9w1"),
        # api_key=os.getenv("UPSTAGE_API_KEY"),
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
        api_key=os.getenv("sk-HTOktt1iYGmU9ZNIdtiSs8XpNM3YCy3tNZFGqa8jvi5HI9w1"),
        base_url="https://pro.xiaoai.plus/v1",
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

        #处理markdown文件
        markdown_file = "./Markdown.md"#替换为你的markdown文件路径
        markdown_content = process_markdown_file(markdown_file)
        await rag.ainsert(markdown_content)


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

        # queryQuestion = 'What is the root locus? Plot the root locus of\
        #       the system step by step according to the principle and steps of\
        #           tracing root locus: $G(s)H(s)=\\frac{K^*}{s^4+4s^3+12s^2+20s+10}$Tracing \
        #             root locus, please give the specific analysis method of each step.'
                # and the formulas involved are listed in LATEX syntax.'
        # 假设我从没学习过自动控制原理，向我解释Figure 1–2 Temperature control system这张图片里的知识细节
        queryQuestion = 'Suppose I have never studied the principles of\
              automatic control, explain to me the details of the knowledge\
                  in the picture Figure 1-2 Temperature control system'
        print("question:",queryQuestion)

        # Perform naive search
        # print("query mode : naive")
        # print(
        #     await rag.aquery(
        #         queryQuestion, param=QueryParam(mode="naive")
        #     )
        # )
        with open("naive.md", "w", encoding="utf-8") as f:
            f.write("query mode : naive\n")
            f.write(await rag.aquery(queryQuestion, param=QueryParam(mode="naive")))


        # Perform local search
        # print("query mode : local")
        # print(
        #     await rag.aquery(
        #         queryQuestion, param=QueryParam(mode="local")
        #     )
        # )
        with open("local.md", "w", encoding="utf-8") as f:
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
        with open("global.md", "w", encoding="utf-8") as f:
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
        with open("hybrid.md", "w", encoding="utf-8") as f:
            f.write("query mode : hybrid\n")
            f.write(await rag.aquery(queryQuestion, param=QueryParam(mode="hybrid")))


    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()  # 打印完整的错误堆栈


if __name__ == "__main__":
    asyncio.run(main())
