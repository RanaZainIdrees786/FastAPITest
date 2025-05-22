import os
from groq import Groq

client = Groq(
    api_key=os.environ.get('GROQ_API_KEY'),
)

prompt_template = "who is the founder of Arfa Karim Technology Incubator"
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

print(response)