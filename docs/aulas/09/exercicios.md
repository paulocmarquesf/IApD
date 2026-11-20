# Aula 09 — Exercícios conceituais

**Resolução individual em papel.** Mostre as contas intermediárias e explicite as hipóteses.

### Exercício 9.1 Ranking de quatro perguntas

Para quatro consultas, o primeiro documento relevante aparece nas posições 1, 4, 2 e não aparece nos dez primeiros. Calcule $\mathrm{MRR}@10$, $\mathrm{Hit}@1$ e $\mathrm{Hit}@5$. Distinga porcentagem de consultas atendidas da posição média do primeiro acerto.

### Exercício 9.2 O MRR distingue rankings

Um buscador recupera o primeiro relevante nas posições 1 e 4 para duas perguntas; outro, nas posições 2 e 2. Calcule o MRR de cada sistema. Qual entrega a resposta mais cedo em uma pergunta e qual é mais uniforme?

### Exercício 9.3 Correspondência exata ou semântica?

Consulta 1: “taxa de administração 0,8%”; consulta 2: “quanto custa manter as cotas?”. Explique por que BM25 pode se destacar na primeira e embeddings na segunda. Não declare superioridade universal de nenhum método.

### Exercício 9.4 Duas classificações, uma fusão

Uma busca lexical ordena $A,B,C$ e uma busca densa ordena $C,A,B$. Pela fusão de postos $\mathrm{RRF}(d)=1/(1+r_1(d))+1/(1+r_2(d))$, calcule os escores dos três documentos. Como desempatar de modo reproduzível?

### Exercício 9.5 O erro do denominador

Em cinco consultas, três têm trechos relevantes identificados no corpus e duas foram classificadas como “sem resposta”. Um relatório calcula Hit@3 = 3/3 e divulga 100% para todas as consultas. Quando o denominador 3 seria aceitável e qual é a taxa no conjunto de cinco consultas?

### Exercício 9.6 Uma política de busca híbrida

Em oito consultas, a busca lexical acerta seis; a densa acerta cinco; os conjuntos de acertos têm quatro consultas em comum. Quantas consultas distintas são atendidas por pelo menos um dos métodos? Calcule o limite máximo de Hit@k de um oráculo que escolhe o melhor dos dois.

### Exercício 9.7: Dois documentos relevantes

Um ranking contém relevantes nas posições 2 e 5. Calcule Hit@3, Recall@3 e RR.

### Exercício 9.8: MRR e primeira posição

Duas consultas têm primeiras evidências nas posições 2 e 4. Calcule MRR.

### Exercício 9.9: Termo raro

Explique por que um identificador exato de fundo pode favorecer BM25 em comparação com embeddings genéricos.

### Exercício 9.10: Paráfrases

Consulta usa “resgate” e documento usa “liquidação de cotas”. Que abordagem pode recuperar a correspondência sem termo idêntico?
