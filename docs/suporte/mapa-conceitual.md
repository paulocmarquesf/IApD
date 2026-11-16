# Mapa conceitual

O curso percorre quatro estágios. Em cada estágio, a pergunta muda: **o que o sistema sabe?** → **o que ele consegue extrair?** → **onde está a evidência?** → **quais ações são permitidas?**

```mermaid
flowchart TD
 A[LLM: tokens e contexto] --> B[Embeddings e similaridade]
 B --> C[Saídas estruturadas]
 C --> D[Classificação e avaliação]
 D --> E[Ferramentas e cálculo]
 E --> F[Aplicações compostas]
 F --> G[RAG: corpus e chunks]
 G --> H[RAG: resposta com citação]
 H --> I[Avaliação: recuperação e geração]
 I --> J[Melhoria controlada]
 J --> K[Workflows e agentes]
 K --> L[Segurança, avaliação e supervisão]
```

| Camada | Pergunta para decidir | Erro típico |
|---|---|---|
| LLM | Há dados suficientes? | Confundir plausibilidade com estimativa |
| Embedding | Qual noção de similaridade é útil? | Confundir proximidade textual com substituição econômica |
| Saída estruturada | O campo existe e está correto? | Confundir JSON válido com fato |
| Ferramentas | O cálculo usa argumentos confiáveis? | Dividir por zero; misturar unidades |
| RAG | A fonte certa foi recuperada? | Citar trimestre errado |
| Avaliação | A evidência sustenta o texto? | Premiar resposta sem apoio documental |
| Agentes | A ação é autorizada? | Obedecer instrução inserida em fonte |
