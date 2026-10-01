from ollama import chat
mesages=[
    {"role":"system","content":"Identify sentiments as positive,negative,neutral.Reply with one word only."},
    {"role":"user","content":"Great movie!"},
    {"role":"System","content":"positive"},
    {"role":"user","content":"waste of money"},
    {"role":"System","content":"negative"},
    {"role":"user","content":"it was ok"},
    {"role":"System","content":"neutral"},
    {"role":"user","content":"Loved the acting but the ending was dull"},
]
response=chat(
    model="llama3.2",
    messages=mesages
)
print(response.message.content)