# RAG-System-for-Fire-Safety-Systems-Documents-Using-DeepSeek-R1
*A Retrieval-Augmented Generation (RAG) prototype for analyzing fire safety documentation, optimized for local execution on M1 Macs*

<img width="1042" alt="Screenshot 2025-02-21 at 3 00 31 AM" src="https://github.com/user-attachments/assets/60336a14-14ed-47f2-859a-352ba59737e1" />

# 🔍 Retrieval-Augmented Generation (RAG) Prototype for Fire Safety Documentation  

This project is a **prototype** designed to demonstrate the power of Retrieval-Augmented Generation (RAG) in answering domain-specific queries and generating personalized recommendations based on client requirements. The system processes large fire alarm documentation, such as the *Simplex 4100ES Fire Control Unit guide*, and uses AI to provide accurate answers and actionable recommendations tailored to user queries.

---

## 🧠 What is RAG?

**Retrieval-Augmented Generation (RAG)** is a hybrid AI technique that combines the strengths of retrieval-based systems and generative models. It retrieves relevant information from a knowledge base (e.g., documents, databases) and augments this information with a Large Language Model (LLM) to generate precise, context-aware responses. Unlike traditional LLMs that rely solely on their training data, RAG dynamically incorporates external domain-specific data, ensuring up-to-date and accurate outputs.

### How RAG Works:
1. **Retrieval**: Identifies relevant documents from a vector database using semantic search.
2. **Augmentation**: Combines retrieved information with the user's query to create a detailed context.
3. **Generation**: Uses an LLM to generate responses based on the augmented query.

---

## 💡 Use Case

This prototype focuses on analyzing fire alarm documentation, such as the *Simplex 4100ES Fire Control Unit guide*. It can:
- Answer technical questions like *"Explain the purpose and operation sequence of Install Mode in 4100ES Fire Control Units."*
- Generate personalized recommendations for configuring fire safety systems based on client-specific requirements.
- Process large documents efficiently to provide accurate, actionable insights.

The ultimate goal is to scale this system to handle massive datasets and deliver tailored recommendations for various industries.

## 🛠️ Installation Guide

### Prerequisites
1. **Python 3.11**  
   Install via Homebrew:  
   `brew install python@3.11`

2. **Ollama**  
   Download from [ollama.ai](https://ollama.ai/download)  
   Verify installation:  
   `ollama --version`

3. **System Requirements**  
   - macOS Ventura or newer  
   - 8GB RAM (16GB recommended)  
   - 2GB free storage

### Setup Steps

**Clone Repository**  
Clone the repository from GitHub and navigate to the project directory:
  `git clone https://github.com/rayidali/fire-safety-rag.git`

**Create Virtual Environment**  
Create a virtual environment using Python 3.11 and activate it:
  `python3 -m venv rag-env`
  `source rag-env/bin/activate`

**Install Python Dependencies**  
Install the required Python packages from the `requirements.txt` file:
  `pip install -r requirements.txt`

Ensure you have a `requirements.txt` file in your project directory with the following content:
  `langchain-huggingface>=0.1.0`
  `chromadb>=0.4.24`
  `python-dotenv>=1.0.0`
  `langchain>=0.2.0`

**Download AI Models**  
Pull the necessary AI models using Ollama:
  `ollama pull deepseek-r1:1.5b`


## 📄 Usage Instructions
1. **Prepare Document**  
   Place your text manual in the project folder as `test1.txt`

2. **Start Ollama Service** (in separate terminal)  
   `ollama serve`

3. **Run Analysis System**  
   `python3 local_rag.py`

## 🔮 Future Improvements
1. **Core Features**  
   - [ ] PDF diagram processing capability  
   - [ ] Multi-document cross-referencing  
   - [ ] Compliance checklist generator  

2. **Interface Enhancements**  
   - [ ] Web-based GUI  

3. **Performance**  
   - [ ] GPU acceleration optimization  
   - [ ] Document version comparison  
   - [ ] Automated update checks  
