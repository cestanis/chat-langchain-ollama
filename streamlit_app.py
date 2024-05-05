import streamlit as st
from langchain.llms import Ollama

st.title("Chat with Me")

def reponse_generator(prompt):
    llm = Ollama(model="dolphin-mistral", temperature=0.7, stop=["AI: "])
    # response = llm(prompt)
    messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
    messages.append({"role": "user", "content": prompt})
    for word in llm.stream(messages):
        yield word


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt :=  st.chat_input("How can I help you today?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    # response = f"Echo: {prompt}"
    with st.chat_message("assistant"):
        response = st.write_stream(reponse_generator(prompt))
    st.session_state.messages.append({"role": "assistant", "content": response})
