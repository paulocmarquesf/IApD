# Folha de consulta

## LLMs e embeddings

- **LLM autoregressivo:** gera cada token condicionado aos anteriores. Maior probabilidade de texto não significa maior probabilidade de fato.
- **Temperatura:** altera dispersão da distribuição de tokens; não é acesso a novas fontes.
- **Similaridade cosseno:** $\cos(u,v)=\frac{u^\top v}{\|u\|\|v\|}$, para $u,v$ não nulos.
- **Busca lexical:** útil com códigos, números, nomes e palavras exatas. **Busca semântica:** útil com paráfrases e descrições.

## Avaliação de classificação

$\text{precisão}=TP/(TP+FP)$; $\text{recall}=TP/(TP+FN)$; $\text{acurácia}=(TP+TN)/(TP+FP+FN+TN)$.

## Finanças e macroeconomia básica

- Retorno simples: $r_t=P_t/P_{t-1}-1$.
- Margem operacional: resultado operacional / receita líquida (período e unidade coerentes).
- Indicador de receita atribuída a uma campanha: (receita atribuída - custo) / custo. **Não é efeito causal por definição.**
- Inflação acumulada: $\prod_t(1+\pi_t)-1$, com $\pi_t$ em proporção.
- Pontos percentuais: diferença entre duas taxas expressas em %; não confundir com variação relativa.

## RAG e agentes

- RAG: documentos → chunks → índice → busca → seleção → contexto → resposta citada.
- **Recall@k:** fração de consultas com fonte relevante entre os k primeiros (sobre perguntas com fonte no corpus).
- **MRR:** média do inverso da posição da primeira fonte relevante; não encontrado contribui com zero.
- **Abstenção:** se não houver fonte suficiente, não inventar.
- **Workflow:** etapas explícitas; **agente:** escolhe ações sob política e limites.
- **Prompt injection:** instrução hostil em dado/documento não deve atravessar fronteira de autoridade.
