import chromadb
import PyPDF2
from sentence_transformers import SentenceTransformer


def extract_text_from_pdf(path):
    with open(path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks    



def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


model = SentenceTransformer("all-MiniLM-L6-v2")  # lightweight and fast
text = extract_text_from_pdf("data/Arfa Karim Technology Incubator.pdf")
chunk_text = chunk_text(text)
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="akti_data")
collection.add(
    documents=[
        "This  is a document about pineapples",
        "This is a document about oranges"
    ],
    ids=["id1", "id2"],
)

results = collection.query(
    query_texts=["pineapples"],
    n_results=2,
)

print(results)





