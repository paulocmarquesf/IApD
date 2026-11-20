# Aula 11 — Atividade feita em casa

**Aplicação:** Workflows e agentes de IA

A atividade utiliza a mesma técnica estudada em aula, com dados diferentes. O uso de ferramentas de IA é permitido, inclusive o Codex em sua interface gráfica. **Não é necessário escrever código nem abrir o terminal.**

**Arquivo inicial:** [`aula_11_pedidos_endereco.csv`](../../dados/casa/aula_11_pedidos_endereco.csv) (pacote sintético). Confira os documentos complementares listados abaixo.

## Enunciado

**Dados.** Simulador alternativo de mudança de endereço pós-compra, com oito pedidos fictícios, política própria e dois caminhos de exceção.

**Questões de interpretação.**

1.  Desenhe o grafo mínimo com seis estados e duas guardas.

2.  Mostre o rastro de uma execução permitida e uma interrompida.

3.  Onde um pedido inexistente deve parar?

4.  Qual transição seria proibida mesmo que o LLM a solicitasse?

**Depósito no GitHub.** `estados.pdf` ou `estados.png`, `rastros.csv`, `interpretacao.md` e `testes.json`. Todos os artefatos serão preparados ou revisados via interface gráfica, sem comandos de terminal.

**Quiz / fechamento.** Estados, guardas, terminação, ferramentas e diferença entre workflow e agente.

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

- [`aula_11_eventos.csv`](../../dados/casa/aula_11_eventos.csv)
- [`aula_11_pedidos_endereco.csv`](../../dados/casa/aula_11_pedidos_endereco.csv)
- [`aula_11_politica_endereco.md`](../../dados/casa/aula_11_politica_endereco.md)
