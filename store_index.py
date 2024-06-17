from src.helper import load_pdf,text_split,embedding
from langchain import embeddings
from langchain.vectorstores import Chroma

extracted_data=load_pdf("data/")
text_chunks=text_split(extracted_data)

persist_directory='db'
vectordb=Chroma.from_documents(documents=text_chunks,embedding=embedding,persist_directory=persist_directory)
