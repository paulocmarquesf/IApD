# Aula 09 — Atividade feita em casa

**Aplicação:** Avaliação da recuperação de informação

A atividade utiliza a mesma técnica estudada em aula, com dados diferentes. O uso de ferramentas de IA é permitido, inclusive o Codex em sua interface gráfica. **Não é necessário escrever código nem abrir o terminal.**

**Arquivo inicial:** [`aula_09_trechos.csv`](../../dados/casa/aula_09_trechos.csv) (pacote sintético). Confira os documentos complementares listados abaixo.

## Enunciado

**Dados.** Novo corpus pequeno de regulamentos fictícios de fundos de investimento com 18 trechos, dez consultas e julgamentos de relevância fornecidos; algumas perguntas são paráfrases.

**Questões de interpretação.**

1.  Calcule manualmente MRR@3 para três consultas e confronte com a aplicação.

2.  Qual estratégia tem maior Hit@3 e em quais consultas perde?

3.  Que tipos de pergunta favorecem BM25 ou recuperação densa nesse corpus?

4.  Há evidência suficiente para recomendar um método em todos os corpora?

**Depósito no GitHub.** `rankings.csv`, `metricas.csv`, `interpretacao.md` e `testes.json`. Todos os artefatos serão preparados ou revisados via interface gráfica, sem comandos de terminal.

**Quiz / fechamento.** Hit@k, MRR, BM25, embeddings e condições de comparação justa.

## Condições mínimas de execução

1. Crie a aplicação por prompts na interface gráfica do Codex e solicite ao agente que execute os testes.
2. Utilize a nova base fornecida, sem substituir silenciosamente dados ausentes por valores inventados.
3. Apresente resultados ligados aos identificadores e às fontes dos registros.
4. Responda por escrito às quatro questões de interpretação, com evidências e eventuais cálculos.
5. Deposite no repositório individual no GitHub os arquivos solicitados e verifique, na interface gráfica, se ficaram disponíveis.

## Entrega e quiz

O depósito no GitHub **não recebe nota**, mas habilita o quiz dos 15 minutos iniciais da aula seguinte. O quiz avaliará os conceitos e as interpretações, não a capacidade de memorizar comandos. A atividade da Aula 12 serve à consolidação da disciplina, sem quiz subsequente previsto.

**Observação sobre dados:** qualquer dado denominado “simulado”, “fictício” ou “didático” foi produzido para ensino e não representa resultados de mercado nem documentos oficiais.


## Arquivos fornecidos

- [`aula_09_consultas.csv`](../../dados/casa/aula_09_consultas.csv)
- [`aula_09_relevancia.csv`](../../dados/casa/aula_09_relevancia.csv)
- [`aula_09_trechos.csv`](../../dados/casa/aula_09_trechos.csv)
