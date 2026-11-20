# Aula 07 — Atividade feita em casa

**Aplicação:** Retrieval-Augmented Generation

A atividade utiliza a mesma técnica estudada em aula, com dados diferentes. O uso de ferramentas de IA é permitido, inclusive o Codex em sua interface gráfica. **Não é necessário escrever código nem abrir o terminal.**

**Arquivo inicial:** [`aula_07_reuniao_A.md`](../../dados/casa/aula_07_reuniao_A.md) (pacote sintético). Confira os documentos complementares listados abaixo.

## Enunciado

**Dados.** Dois documentos didáticos fictícios de reuniões monetárias, identificados e datados, acompanhadas de oito perguntas que exigem distinguir reuniões e justificar citações.

**Questões de interpretação.**

1.  Qual trecho responde a cada uma das duas perguntas mais difíceis e por quê?

2.  O que se perde ao reduzir k de 3 para 1?

3.  Apresente um caso de referência temporal incorreta e sua correção.

4.  Em qual pergunta o sistema deveria abster-se?

**Depósito no GitHub.** `recuperacao.csv` com ID/data/trecho, `respostas.md`, `interpretacao.md` e `testes.json`. Todos os artefatos serão preparados ou revisados via interface gráfica, sem comandos de terminal.

**Quiz / fechamento.** Chunking, top-k, fundamentação, citações e distinção entre falha de recuperação e de geração.

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

- [`aula_07_perguntas.csv`](../../dados/casa/aula_07_perguntas.csv)
- [`aula_07_reuniao_A.md`](../../dados/casa/aula_07_reuniao_A.md)
- [`aula_07_reuniao_B.md`](../../dados/casa/aula_07_reuniao_B.md)

Os dois documentos de reuniões monetárias são **fictícios**. Uma versão com atas oficiais somente poderá ser utilizada após curadoria documental e verificação das fontes.
