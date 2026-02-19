# 🧠 AI Wellness Coach (RAG Powered)

An AI-powered mental wellness assistant that provides emotional support, stress management, anxiety reduction, and motivation coaching using Large Language Models and Retrieval-Augmented Generation (RAG).

This project combines natural language processing, vector search, and a conversational interface to deliver evidence-based wellness guidance.

---

## 🚀 Features

- 💬 Chat-based emotional support interface
- 🧠 Burnout, anxiety, and motivation detection
- 📚 Knowledge-based responses using RAG
- 🔍 Semantic search with FAISS
- ⚡ Fast and responsive Gradio UI
- 🔐 Ethical and safety-focused design
- 🌐 Hugging Face deployment ready

---

## 🏗️ System Architecture

User Input
↓
Gradio Interface
↓
Embedding Model (MiniLM)
↓
FAISS Vector Database
↓
Context Retrieval
↓
LLM (Phi-1.5)
↓
AI Response

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| LLM | Microsoft Phi-1.5 |
| Embeddings | Sentence-Transformers (MiniLM) |
| Vector DB | FAISS |
| UI | Gradio |
| Framework | Hugging Face Transformers |

---

## 📁 Project Structure

ai-wellness-coach/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│ └── wellness_docs.txt
└── venv/ (optional)

---

## ☁️ Deployment (Hugging Face Spaces)

1. Create a new Space (Gradio type)
2. Upload `app.py`, `requirements.txt`, and `data/`
3. Hugging Face will automatically install dependencies
4. App will be live within minutes

---

## ⚠️ Disclaimer

This application is intended for informational and emotional support purposes only. It is not a substitute for professional medical or psychological advice, diagnosis, or treatment.

If you are experiencing severe distress, please consult a qualified healthcare professional.

---

## 📈 Future Enhancements

- User mood tracking
- Burnout scoring system
- Weekly wellness reports
- PDF document ingestion
- Personalized coaching plans
- Multi-language support

---

## 👨‍💻 Author

Developed by: **Sugnik Mondal**

MBA | Data Science | AI Enthusiast

LinkedIn: <your-link-here>

---

## 📜 License

This project is released under the MIT License and is free to use for educational purposes.
