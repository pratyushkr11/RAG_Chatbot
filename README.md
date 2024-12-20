# RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built to provide intelligent and context-aware answers to user queries about various products. This chatbot combines semantic search capabilities with a generative language model to deliver accurate and comprehensive responses.

---

## Features

- **Product Query Handling**: Retrieve and answer user questions about product specifications, pricing, and availability.
- **RAG Integration**: Combines retrieval of relevant documents with generative AI for precise and informative responses.
- **Session Management**: Maintains chat history for a seamless conversational experience.
- **Streamlit Interface**: Provides a user-friendly web interface for real-time interaction.

---

## Application

### Live Application Link:
Access the live application [here](https://ragchatbot-gdsw83ggwg856jlmsscd4e.streamlit.app/).

---

## Installation

Follow the steps below to set up and run the chatbot locally:

### 1. Clone the Repository
```bash
git clone https://github.com/pratyushkr11/RAG_Chatbot.git
cd RAG_Chatbot
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 3. Install Dependencies
Install the required libraries using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add the following:
```env
GOOGLE_API_KEY=your_google_genai_api_key
```

Replace `your_google_genai_api_key` with your Google Generative AI API key.

### 5. Run the Application
Start the Streamlit app:
```bash
streamlit run app.py
```

---

## Repository Structure

```
RAG_Chatbot/
├── app.py                 # Main Streamlit application
├── chatbot.py             # Core logic for the chatbot
├── prompts.py             # Prompt templates for the LLM
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not included in repo)
├── data/                  # Folder for product data (e.g., JSON files)
└── chromaDB/              # Folder for Chroma database persistence
```

---

## Usage

1. Launch the application using the live link or locally using Streamlit.
2. Type your question about a product in the input field.
3. Receive intelligent, context-aware responses powered by RAG.

---

## Technologies Used

- **Google Generative AI (Gemini)**: For embeddings and generative language model capabilities.
- **LangChain**: Framework for integrating RAG workflows and chain building.
- **Chroma**: Vector database for efficient storage and retrieval of embeddings.
- **Streamlit**: Interactive web application framework for a user-friendly interface.

---

## Contributing

Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## Contact

For any questions or feedback, feel free to reach out:
- **Email**: krpratyush4813@gmail.com
- **GitHub**: [pratyushkr11](https://github.com/pratyushkr11)
