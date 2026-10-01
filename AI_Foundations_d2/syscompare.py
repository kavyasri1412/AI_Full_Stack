from ollama import chat
roles=[
    "you are a strict math teacher.Answer briskly and in one line.",
    "you rae a movie director.Answer in a filmy way,answer in 2 lines",
    "you are a lawyer.Answer professionally.One line answer"
]
for role in roles:
    response=chat(
        model="llama3.2",
        messages=[
            {
                "role":"system",
                "content":role
            },
            {
                "role":"user",
                "content":"how many colours in the rainbow"
            }
        ]
    )
    print(f"---{role}---")
    print(response.message.content)
    print()