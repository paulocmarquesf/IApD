"""Referência técnica para inspeção pelo Codex; não contém credenciais."""
import os
from openai import OpenAI

def call_model(prompt: str) -> str:
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY ausente; use o modo local da aula")
    client = OpenAI()
    model = os.environ.get("OPENAI_MODEL", "gpt-5.5")
    response = client.responses.create(model=model, input=prompt)
    return response.output_text

if __name__ == "__main__":
    print(call_model("Explique, em uma frase, o que é uma evidência documental."))
