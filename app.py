import gradio as gr
import torch
import faiss
import os

from transformers import AutoModelForCasualLM, AutoTokenizer
from sentence_transformers import SentenceTransformer


# Loading Models

model_name = "microsoft/phi-1_5"
embed_name = "sentence-transformers/all-MiniLM-L6-v2"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCasualLM.from_pretrained(
    model_name,
    torch_dtype = torch.float32,
    device_map = "auto"
)

embedder = SentenceTransformer(embed_name)


# Load Documents

def load_documents(file_path):

    with open(file_path, "r", encoding = "utf-8") as f:
        text = f.read()

    chunks = text.split("\n")

    return [c.strip() for c in chunks if len(c) > 20]

docs = load_documents("data/wellness_docs.txt")


# Create Vector DB (FAISS)

doc_embeddings = embedder.encode(docs)

dimension = doc_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)


# Retrieve Context

def retrieve_context(query, k=3):

    q_embed = embedder.encode([query])

    distances, indices = index.search(q_embed, k)

    results = []

    for i in indices[0]:
        results.append(docs[i])

    return "\n".join(results)


# Generate Response (RAG)

def generate_wellness_response(user_input):

    context = retrieve_context(user_input)

    prompt = f"""
You are an empathetic AI wellness coach.

Use the information below to help the user.

Context:
{context}

Rules:
- Be kind and supportive
- Do not diagnose
- Do not prescribe medicine
- Encourage healthy habits
- Suggest professional help if needed

User Message: {user_input}

Response:
"""
    
    inputs = tokenizer(prompt, return_tensors = "pt")

    with torch.no_grad():

        output = model.generate(
            **inputs,
            max_new_tokens = 300,
            do_samples = True,
            top_k = 50,
            top_p = 0.9,
            temperature= 0.7
        )

    response = tokenizer.decode(output[0], skip_special_tokens = True)

    return response.replace(prompt, "").strip()


# Wrapper

def wellness_chatbot(user_input):

    return generate_wellness_response(user_input)



# UI

with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown(
        """
        # 🧠 AI Wellness Coach (RAG Powered)

        Your personal assistant for managing stress, anxiety, burnout, and motivation.

        ⚠️ *This tool is for emotional support only and not a replacement for professional care.*
        """
    )

    chatbot = gr.Chatbot(
        height=450,
        show_copy_button=True
    )

    state = gr.State([])

    with gr.Row():

        txt = gr.Textbox(
            placeholder="Type how you're feeling...",
            lines=2,
            scale=4
        )

        send_btn = gr.Button("Send", scale=1)

    with gr.Row():
        clear_btn = gr.Button("Clear Chat")


    # chat Logic

    def respond(message, history):

        reply = wellness_chatbot(message)

        history.append((message, reply))

        return "", history


    send_btn.click(
        respond,
        inputs=[txt, state],
        outputs=[txt, chatbot]
    )

    txt.submit(
        respond,
        inputs=[txt, state],
        outputs=[txt, chatbot]
    )

    clear_btn.click(
        lambda: [],
        outputs=chatbot
    )


# Main

if __name__ == "__main__":
    demo.launch()