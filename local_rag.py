import os
from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma  # Using Chroma instead of FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Configuration
TXT_PATH = "test1.txt"
MODEL_NAME = "deepseek-r1:1.5b"
CHROMA_DIR = "book_chroma_db"  # Persistent storage

def main():
    # M1 optimization
    os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"
    
    if not Path(TXT_PATH).exists():
        print(f"❌ Error: {TXT_PATH} not found")
        return

    try:
        # Load and process document
        loader = TextLoader(TXT_PATH)
        docs = loader.load()
        
        # Text splitting optimized for M1
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=512,
            chunk_overlap=64,
            separators=["\n\n", "\n", ". "]
        )
        documents = text_splitter.split_documents(docs)

        # Initialize embeddings with explicit model name
        embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        
        # Create Chroma vector store
        vector_store = Chroma.from_documents(
            documents=documents,
            embedding=embedder,
            persist_directory=CHROMA_DIR
        )
        
        # Configure retriever with score threshold
        retriever = vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={"k": 4, "score_threshold": 0.12}
        )

        # Initialize LLM
        llm = Ollama(model=MODEL_NAME)

        # Create RAG chain
        qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={
                "prompt": PromptTemplate.from_template(
                    """Analyze this text file:
                    {context}
                    
                    Question: {question}
                    Focus on products and features in your answer:"""
                )
            }
        )

        # Execute query
        question = "Explain the purpose and operation sequence of Install Mode in 4100ES Fire Control Units"
        result = qa({"query": question})
        
        print(f"\n🧠 Question: {question}")
        print(f"\n📝 Answer: {result['result']}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Troubleshooting steps:")
        print("1. Ensure Python 3.11 is used (brew install python@3.11)")
        print("2. Run: pip install langchain-huggingface chromadb")
        print("3. Verify Ollama is running: ollama serve")

if __name__ == "__main__":
    main()







