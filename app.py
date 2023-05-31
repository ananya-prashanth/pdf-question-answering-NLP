from flask import Flask, render_template, request
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "your-API-key"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    question = request.form['question']
    chat_history = request.form.getlist('chat_history[]')  # Get the chat history as a list
    # Save the uploaded file to a temporary location
    file_path = 'templates/' + file.filename
    file.save(file_path)

    # Load the document
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    # Select which embeddings we want to use
    embeddings = OpenAIEmbeddings()

    # Create the vector store to use as the index
    db = Chroma.from_documents(texts, embeddings)

    # Create a ConversationalRetrievalChain to generate answers
    qa = ConversationalRetrievalChain.from_llm(OpenAI(), db.as_retriever(search_type="similarity", search_kwargs={"k": 2}))

    # Generate the answer using the ConversationalRetrievalChain
    answer = generate_answer(question, chat_history, qa)

    return render_template('result.html', answer=answer)

def generate_answer(question, chat_history, qa):
    # Generate the answer using the ConversationalRetrievalChain
    result = qa({"question": question, "chat_history": chat_history})

    # Extract the generated answer
    answer = result["answer"]

    return answer

if __name__ == '__main__':
    app.run()
