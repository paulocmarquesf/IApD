"""Referência para execução supervisionada com sessão Codex autenticada.
O SDK do Codex serve para executar tarefas em threads; não é a API de modelos.
O aluno pede ao Codex para executar/adaptar o exemplo, sem editar código.
"""
from openai_codex import Codex, Sandbox

def supervised_turn(prompt: str) -> str:
    with Codex() as codex:
        thread = codex.thread_start(sandbox=Sandbox.read_only)
        result = thread.run(prompt)
        return result.final_response

if __name__ == "__main__":
    print(supervised_turn("Explique o conceito de golden set em duas frases."))
