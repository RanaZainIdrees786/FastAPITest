import requests

def query_ollama(prompt, model="llama3.2:latest"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    return response.json()["response"]

# Example usage
reply = query_ollama("What is the capital of France?")
print("Ollama says:", reply)