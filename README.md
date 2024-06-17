# Chatbot-using-llama2
Chatbot using llama2  


I've implemented a local flask web application using langchain and llama2 that can integrate text-input, retrieving embeddings from a vector db and generates the response using a language model. Here, everything is done locally, you can use it for internal purposes.  


## Steps for implementation  

Download the llm from below link  
select the llama-2-7b-chat.ggmlv3.q4_0.bin for the download.  

https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main  

### Install required packages

To install required packages and libraries, run the below command  
``` pip install -r requirements.txt ```  

### Load the data from pdf's  and store it in vector db.  
To load the data from pdf's convert the text into chunks, and later convert those text-chunks to embeddings.  

Create a data folder and place the pdf file in that folder.  

To convert the text chunks to embeddings and store it in chroma db, run store_index.py file.  

finally, run the app.py to interact with the chatbot.







