from ollama import chat
response=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"i am the principle of the womens college there is an an women oriented program tommorow can you prepare a speech for the tommorow program "
        }
    ]
)
print(response.message.content)