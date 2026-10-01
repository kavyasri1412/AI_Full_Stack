from ollama import chat
import streamlit as st

st.set_page_config(page_title="LlamaBot App", page_icon="🤖")
st.title("LlamaBot ")

personality = " you are a friendly and patient tutor name Llama .answer warmly .keep the answer in one sentence "

personality_2="You are a funny and quirky tutor.Say me joke related to the question I have asked"
if "history" not in st.session_state:
    st.session_state.history = [{"role": "system", "content": personality}]

if "toast_msg" not in st.session_state:
    st.session_state.toast_msg=None

if st.session_state.toast_msg:
    st.toast(st.session_state.toast_msg[0],icon=st.session_state.toast_msg[1])
    st.session_state.toast_msg=None

with st.sidebar:
    st.header("chat controls")
    if st.button("clear chat",type="primary"):
        st.session_state.history=[{"role":"system","content":personality}]
        st.session_state.toast_msg=("chat cleared successfully!","🗑️")
        st.rerun()
    if st.button("change personality"):
        st.session_state.history[0]["content"]=personality_2
        st.session_state.toast_msg=("Bot personality changed successfully!","👍")
        st.rerun()


with st.chat_message("assistant"):
    st.write("Hello! I am Llama, your friendly tutor. How can I assist you today?")

for message in st.session_state.history[1:]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask Anything", key="input")
if question := user_input:
    st.session_state.history.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)
    try:
        with st.spinner("Thinking..."):
            response=chat(model="llama3.2",messages=st.session_state.history)
        reply=response["message"]["content"]
        st.session_state.history.append({"role":"assistant","content":reply})

        with st.chat_message("assistant"):
            st.write(reply)
    except Exception as e:
        st.write("ollama is not working.Try Again!!")

