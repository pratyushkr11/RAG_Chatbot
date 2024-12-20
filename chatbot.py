from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.runnables.history import RunnableWithMessageHistory
from prompts import contextualize_q_system_prompt, chatbot_prompt
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state:
        st.session_state[session_id] = ChatMessageHistory()
    return st.session_state[session_id]


def create_vectorstore_retriever(collection_name, k=10):
    # Initialize the vectorstore with the given collection name
    vectorstore = Chroma(
        persist_directory="./chromaDB",
        collection_name=collection_name,
        embedding_function=embeddings,
    )
    
    # Create the retriever with the specified 'k' value
    retriever = vectorstore.as_retriever(search_kwargs={'k': k})

    return retriever

def run_main_conversational_rag_chain(retriever,question,session_id):
    
    # Create the contextualize_q_prompt
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    # Create history-aware retriever
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )

    # Create the qa_prompt
    final_chatbot_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", chatbot_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    # Create the question-answer chain
    question_answer_chain = create_stuff_documents_chain(llm, final_chatbot_prompt)

    # Create the RAG chain
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )

    # Get the session history
    history = get_session_history(session_id)

    # Prepare the inputs
    inputs = {"input": question, "chat_history": history.messages}
    config = {"configurable": {"session_id": session_id}}

    # Invoke the chain and get the response
    response = conversational_rag_chain.invoke(inputs, config=config)

    output = {
        "answer": response['answer'],
    }
    return output