import os

from lightrag import LightRAG, QueryParam
from lightrag.llm import hf_model_complete, hf_embedding
from lightrag.utils import EmbeddingFunc
from transformers import AutoModel, AutoTokenizer
# 在代码开头添加
import torch

print("CUDA是否可用:", torch.cuda.is_available())
print("当前设备:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU")

WORKING_DIR = "./hf20250102"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)


rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=hf_model_complete,
    llm_model_name="meta-llama/Llama-3.1-8B",
    embedding_func=EmbeddingFunc(
        embedding_dim=1536,
        max_token_size=5000,
        func=lambda texts: hf_embedding(
            texts,
            tokenizer=AutoTokenizer.from_pretrained(
                "answerdotai/ModernBERT-base"
            ),
            embed_model=AutoModel.from_pretrained(
                "answerdotai/ModernBERT-base"
            ),
        ),
    ),
)
# rag = LightRAG(
#     working_dir=WORKING_DIR,
#     chunk_token_size = 8000,
#     llm_model_func=hf_model_complete,
#     llm_model_name="THUDM/chatglm2-6b",
#     embedding_func=EmbeddingFunc(
#         embedding_dim=1536,
#         max_token_size=5000,
#         func=lambda texts: hf_embedding(
#             texts,
#             tokenizer=AutoTokenizer.from_pretrained(
#                 "answerdotai/ModernBERT-base"
#             ),
#             embed_model=AutoModel.from_pretrained(
#                 "answerdotai/ModernBERT-base"
#             ),
#         ),
#     ),
# )


# with open("./book.txt", "r", encoding="utf-8") as f:
#     rag.insert(f.read())


#处理单个markdown文件
def process_markdown_file(file_path):
    with open(file_path,"r",encoding="utf-8")as f:
        return f.read()
    
#处理markdown文件
markdown_file = "./Markdown.md"#替换为你的markdown文件路径
markdown_content = process_markdown_file(markdown_file)
rag.insert(markdown_content)




# Perform naive search
print(
    rag.query("What are the top themes in this story?", param=QueryParam(mode="naive"))
)

# Perform local search
print(
    rag.query("What are the top themes in this story?", param=QueryParam(mode="local"))
)

# Perform global search
print(
    rag.query("What are the top themes in this story?", param=QueryParam(mode="global"))
)

# Perform hybrid search
print(
    rag.query("What are the top themes in this story?", param=QueryParam(mode="hybrid"))
)
