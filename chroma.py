import chromadb
from readData import read_pdf_data

akti_data = read_pdf_data('data/Arfa Karim Technology Incubator.pdf')
# chunk_size = int(input("Enter chunk size in characters: "))
chunk_size = 100
chunks = [akti_data[i:i+chunk_size] for i in range(0, len(akti_data), chunk_size)]
print(f"Chunks: {len(chunks)}")

chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_or_create_collection(name="akti_data")

# Clean old data if needed
all_ids = collection.peek(10)["ids"]
if all_ids:
    collection.delete(ids=all_ids)

collection.add(
    documents=chunks,
    ids=[str(i) for i in range(len(chunks))],
    metadatas=[{"source": "arfa_pdf"}] * len(chunks)
)

while True:
    query = input("Enter your query: ")
    results = collection.query(
        query_texts=[query],
        n_results=5,
        where={"source": "arfa_pdf"}
    )
    for chunk in results['documents'][0]:
        print(chunk)
        print(50*"=")
    
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != "y":
        break
