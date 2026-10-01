from ollama import chat
bad="Tell me about birds."
good="list about 3 different birds that are suitable for as a pet.2 lines each "
responseB=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":bad
        }
    ]
)
responseG=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":good
        }
    ]
)
print(f"Bad prompt Result:{responseB.message.content}")
print()
print(f"Good prompt Result:{responseG.message.content}")