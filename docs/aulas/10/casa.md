# Aula 10 — Atividade feita em casa

**Aplicação:** Avaliação experimental de aplicações de IA

A atividade utiliza a mesma técnica estudada em aula, com dados diferentes. O uso de ferramentas de IA é permitido, inclusive o Codex em sua interface gráfica. **Não é necessário escrever código nem abrir o terminal.**

**Arquivo inicial:** [`aula_10_apos_rag.csv`](../../dados/casa/aula_10_apos_rag.csv) (pacote sintético). Confira os documentos complementares listados abaixo.

## Enunciado

**Dados.** Novo conjunto com 30 solicitações e regras fictícias de assistência técnica; saídas pareadas A/B e tempos medidos fornecidos pelo professor.

**Questões de interpretação.**

1.  Quantas melhorias e regressões ocorreram, e qual o ganho líquido?

2.  A alteração melhora a taxa de fundamentação? Mostre duas evidências.

3.  Um ganho agregado compensa os erros graves novos? Argumente.

4.  Que aspecto do desenho experimental impediria identificar a causa de uma mudança?

**Depósito no GitHub.** `comparacao.csv`, `regressoes.csv`, `interpretacao.md` e `testes.json`. Todos os artefatos serão preparados ou revisados via interface gráfica, sem comandos de terminal.

**Quiz / fechamento.** Experimentos pareados, baseline, diferenças absolutas/relativas e limites de LLM-as-a-Judge.

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

- [`aula_10_apos_rag.csv`](../../dados/casa/aula_10_apos_rag.csv)
- [`aula_10_comparacao.csv`](../../dados/casa/aula_10_comparacao.csv)
- [`aula_10_politicas.md`](../../dados/casa/aula_10_politicas.md)
