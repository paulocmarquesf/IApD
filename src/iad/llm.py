"""Chamada externa explicitamente opt-in. Não é necessária aos exercícios obrigatórios."""
from __future__ import annotations
import os

def call_llm(prompt,*,model='gpt-4.1-mini'):
    """Faz uma chamada apenas quando existe OPENAI_API_KEY e a lib openai está instalada.

    Atenção: usar este método implica envio do prompt a provedor externo.
    Nunca enviar dados pessoais, credenciais ou documentos confidenciais.
    """
    if not os.getenv('OPENAI_API_KEY'):
        raise RuntimeError('Configure OPENAI_API_KEY apenas se quiser testar a extensão opcional.')
    try:
        from openai import OpenAI
    except ImportError as e:
        raise RuntimeError('Extensão opcional requer: pip install openai') from e
    client=OpenAI()
    r=client.responses.create(model=model,input=prompt)
    return r.output_text
