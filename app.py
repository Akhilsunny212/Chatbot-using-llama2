from flask import Flask, render_template, jsonify, request
from src.helper import embedding
from langchain import embeddings
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from src.prompt import *
app=Flask(__name__)
persist_directory='db'
vectordb=Chroma(persist_directory=persist_directory,embedding_function=embedding)


PROMPT=PromptTemplate(template=prompt_template,input_variables=["context","question"])
chain_type_kwargs={"prompt":PROMPT}

llm=CTransformers(model="Model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.8})


qa=RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectordb.as_retriever(search_kwargs={'k':2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get",methods=["GET","POST"])
def chat():
    msg=request.form["msg"]
    input=msg
    print(input)
    result=qa({"query":input})
    print("Response: ",result["result"])
    return str(result["result"])

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
