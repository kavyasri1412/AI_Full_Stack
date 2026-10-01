from ollama import chat
prompt="give me a 1 line tagline for my coffee shop.Answer in 1 line only the tagline."
for t in [0,0.7,1.5]:
    print(f"Temp:{t}")
    for run in range(3):
        response=chat(
            model="llama3.2",
        messages=[
            {
                "role":"user",
                "content" : prompt
            }
        ],
        options={"temperature":t}
        )
        print(f"Run{run+1}:{response.message.content}")
        print()