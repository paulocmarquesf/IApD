# Aula 05 — Atividade feita em casa

**Aplicação:** Integração de ferramentas computacionais

A atividade utiliza a mesma técnica estudada em aula, com dados diferentes. O uso de ferramentas de IA é permitido, inclusive o Codex em sua interface gráfica. **Não é necessário escrever código nem abrir o terminal.**

**Arquivo inicial:** [`aula_05_precos_18_meses.csv`](../../dados/casa/aula_05_precos_18_meses.csv) (pacote sintético). Confira os documentos complementares listados abaixo.

## Enunciado

**Dados.** Outra base sintética com duas classes de ativos, 18 meses de preços e taxa de referência compatível com a frequência dos retornos.

**Questões de interpretação.**

1.  Compare manualmente um retorno mensal com o calculado pelo sistema.

2.  Qual carteira maximiza Sharpe dentro da grade especificada e qual a sensibilidade à taxa livre de risco?

3.  Verifique como uma data ausente altera o conjunto de retornos válidos.

4.  Que afirmação do texto gerado depende de cálculo e qual depende de hipótese?

**Depósito no GitHub.** `carteiras.csv`, `fronteira.png`, `interpretacao.md` e `testes.json`. Todos os artefatos serão preparados ou revisados via interface gráfica, sem comandos de terminal.

**Quiz / fechamento.** Retornos, covariância, volatilidade, Sharpe e trilha de execução de ferramentas.

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

- [`aula_05_precos_18_meses.csv`](../../dados/casa/aula_05_precos_18_meses.csv)
- [`aula_05_taxa_referencia.csv`](../../dados/casa/aula_05_taxa_referencia.csv)
