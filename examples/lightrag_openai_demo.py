import os

from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete

WORKING_DIR = "./automation"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=gpt_4o_mini_complete,
    llm_model_func=gpt_4o_mini_complete,
    # llm_model_func=gpt_4o_complete
)


# with open("./book.txt", "r", encoding="utf-8") as f:
#     rag.insert(f.read())

#-------------------------------------------------------------
# pdf文件导入
from pypdf import PdfReader

file_path = 'pdfTest.pdf'
reader = PdfReader(file_path)
text_content = ""
for page in reader.pages:
    text_content += page.extract_text()

rag.insert(text_content)

#----------------------------------------------------------------
queryQuestion = "what is Open-Loop Control ?"
# Perform naive search
print("question:",queryQuestion)
print("query mode : naive")
print(
    rag.query(queryQuestion, param=QueryParam(mode="naive"))
)

# Perform local search
print("query mode : local")
print(
    rag.query(queryQuestion, param=QueryParam(mode="local"))
)

# Perform global search
print("query mode : global")
print(
    rag.query(queryQuestion, param=QueryParam(mode="global"))
)

# Perform hybrid search
print("query mode : hybrid")
print(
    rag.query(queryQuestion, param=QueryParam(mode="hybrid"))
)