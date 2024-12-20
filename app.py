__import__('pysqlite3')
import sys
import streamlit as st
from dotenv import load_dotenv
from chatbot import run_main_conversational_rag_chain, create_vectorstore_retriever
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

def response_generator(query):

    retriever = create_vectorstore_retriever("products_db", k=10)

    session_id = "chatbot_conversation_session"

    res = run_main_conversational_rag_chain(retriever, query, session_id)

    response = res["answer"]

    return response

def main():

    if "gemini_model" not in st.session_state:
        st.session_state["gemini_model"] = "gemini-2.0-flash-exp"

    st.title("Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Enter Your Query"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"AI Assistant: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = response_generator(prompt)
            st.write(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()