# pdf-question-answering-NLP
This project leverages LangChain, Agent and OpenAI to input a PDF and when a question is asked, based on the context of the provided PDF, it gives you the corresponding answer.
![image](https://github.com/ananya-prashanth/pdf-question-answering-NLP/assets/87328350/f6ba71ee-f239-45c4-b591-f090f4fb923c)

The goal of this project is to create a web application that allows users to upload PDF files and ask questions related to the content of those files. The application utilizes the LangChain library, which is a Python-based framework for natural language processing tasks.

The application is built using the Flask framework, a lightweight web framework for Python. Flask provides the necessary infrastructure for handling HTTP requests and responses, allowing us to create the user interface and handle file uploads.

When a user uploads a PDF file, the application saves the file to a temporary location. It then uses the LangChain library to process the file and extract the text content. To achieve this, the PyPDFLoader from LangChain is used to load the PDF document, and the CharacterTextSplitter is used to split the document into smaller chunks for analysis.

Next, the application creates an index using the Chroma vector store from LangChain. This index is used to retrieve relevant information based on user queries. The OpenAIEmbeddings class is used to select the embeddings to be used for similarity search within the index.

To generate answers to user questions, the application utilizes the ConversationalRetrievalChain class from LangChain. This class combines the power of the OpenAI GPT-3.5 language model with the indexed documents to provide conversational capabilities. The OpenAI GPT-3.5 model is accessed through the OpenAI API, and the chat history is maintained to provide context for generating accurate answers.

When a user submits a question, the application passes the question and chat history to the ConversationalRetrievalChain, which generates the answer using the OpenAI GPT-3.5 model. The generated answer is then displayed to the user through the web interface.

The user interface consists of two HTML templates: index.html and result.html. The index.html template provides a form for uploading PDF files and submitting questions. The result.html template displays the generated answer to the user.

To run the application, the Flask development server is started, and the application listens for incoming requests. Users can access the application through a web browser and interact with the provided interface.

##how to run:
###clone the repo: 
```
git clone https://github.com/ananya-prashanth/PDF-question-answering-NLP.git
```
###running the Flask app:
```
pip install -r requirements.txt
python app.py
```

