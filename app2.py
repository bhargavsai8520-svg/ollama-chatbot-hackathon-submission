import requests
import gradio as gr

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def query_ollama(model, prompt):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()
    result = response.json()
    return result.get("response", "")

with gr.Blocks(title="Ollama Chat") as demo:
    gr.Markdown("## 🦙 Ollama + Gradio Chat")

    model_name = gr.Textbox(
        label="Model Name",
        value="tinyllama",
        placeholder="e.g. tinyllama, llama2, mistral"
    )

    user_prompt = gr.Textbox(
        label="Prompt",
        placeholder="Ask something...",
        lines=4
    )

    output = gr.Textbox(
        label="Response",
        lines=10
    )

    submit_btn = gr.Button("Generate")

    submit_btn.click(
        fn=query_ollama,
        inputs=[model_name, user_prompt],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch()

