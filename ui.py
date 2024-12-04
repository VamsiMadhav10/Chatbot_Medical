import streamlit as st
import random
import time
import language 
import mapping
# Streamed response emulator
def response_generator(query,location):
    # Simulate generating a response
    response = language.generator(query,location)
    time.sleep(0.05)
    return response

st.title("GlaucoBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):

    print(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display assistant response
    with st.chat_message("assistant"):
        doc=mapping.doc_retrieve(prompt)
        response = response_generator(prompt,str(doc))
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
