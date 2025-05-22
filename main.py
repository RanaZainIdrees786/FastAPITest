from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from readData import read_excel_data
from readData import read_pdf_data
from groq import Groq
import os
import requests
import chromadb

# create a fast api 
app = FastAPI()

# create a groq client
client = Groq(
    api_key=os.environ.get('GROQ_API_KEY'),
)

# read pdf data 
akti_data = read_pdf_data('data/Arfa Karim Technology Incubator.pdf')

# make chunks of whole data
chunk_size = 500
chunks = [akti_data[i:i+chunk_size] for i in range(0, len(akti_data), chunk_size)]

# create chrome client
chroma_client = chromadb.PersistentClient(path="chroma_db")

# create collection
collection = chroma_client.get_or_create_collection(name="akti_data")

# Clean old data if needed
all_ids = collection.peek(10)["ids"]
if all_ids:
    collection.delete(ids=all_ids)

# adding chunks to collection
collection.add(
    documents=chunks,
    ids=[str(i) for i in range(len(chunks))],
    metadatas=[{"source": "arfa_pdf"}] * len(chunks)
)

# Enable frontend connections (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def query_ollama(prompt, model="llama3.2:latest"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    return response.json()["response"]


@app.get("/")
def hello_world():
    return "hello world hala"




# Simple chatbot logic using query parameter ?q=hello
@app.get("/chat")
def simple_chatbot(q: str):
    user_question = q.lower().strip()

    # Find Relevant Chunks From 
    results = collection.query(
        query_texts=[user_question],
        n_results=3,
        where={"source": "arfa_pdf"}
    )
    related_chunks = results['documents'][0]
    akti_info = ""
    for chunk in related_chunks:
        akti_info = akti_info + "\n" + chunk

    for idx, chunk in enumerate(related_chunks):
        print(f"Chunk No:{idx + 1} ")
        print(50*"=")
        print(chunk)
        print(50*"=")


    # akti_info = read_pdf_data('data/Arfa Karim Technology Incubator.pdf')
    courses_info = read_excel_data('data/Courses.xlsx')
    with open('rules.txt', 'r') as file:
        rules = file.read()

    prompt_template = f"""
            Rules:            
            {rules}

            Context:
                Courses: 
                {courses_info}

                AKTI INFO:
                {akti_info}

            User Question:    
            {user_question}            
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt_template,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    response  = chat_completion.choices[0].message.content
    return {"reply": response}
