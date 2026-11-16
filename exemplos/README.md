# Integrações avançadas (opcionais)

Estes exemplos correspondem a **frameworks**, não a requisitos para compreender o conteúdo. Para experimentá-los:

```bash
python -m pip install -e '.[llm]'
```

`demo_langchain.py`: sequência `prompt -> modelo -> parser` com LangChain (exige `OPENAI_API_KEY`).

`demo_chroma.py`: vetores com Chroma local, usando função de embedding **determinística somente para ensaiar a API**, não um embedding semântico; observe que a demonstração não valida resultados de busca em linguagem natural. Para semântica real, configure um modelo de embeddings adequado.

`demo_langgraph.py`: workflow mínimo com `StateGraph`, sem qualquer chamada a API.

**Não envie dados privados ou credenciais ao provedor.**
