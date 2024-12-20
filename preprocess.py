from langchain_chroma import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import JSONLoader
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def insert_vector_data(file_path, collection):
    """
    Load data from JSON and insert each entry into the Chroma vector database one by one.
    """
    # Load JSON data
    loader = JSONLoader(
        file_path=file_path,
        jq_schema='.products[]',  # Parse each product entry
        text_content=False
    )
    data = loader.load()

    # print(data[10].page_content)

    # Initialize Chroma
    vectorstore = Chroma(
        embedding_function=embeddings,
        persist_directory="./chromaDB",
        collection_name=collection,
        collection_metadata={"hnsw:space": "cosine"}
    )

    # Iterate through each document and add it to the vectorstore
    for doc in data:
        # print(doc.metadata)
        try:
            vectorstore.add_texts(
                texts=[doc.page_content]
            )
            print(f"Inserted: {doc.metadata.get('seq_num', 'Unknown')}")
        except Exception as e:
            print(f"Error inserting document: {doc.metadata.get('seq_num', 'Unknown')}. Error: {e}")

insert_vector_data("./data/retail_products.json", "products_db")