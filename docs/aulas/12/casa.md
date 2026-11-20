# Aula 12 — Atividade feita em casa

**Aplicação:** Confiabilidade e segurança de agentes

A atividade utiliza a mesma técnica estudada em aula, com dados diferentes. O uso de ferramentas de IA é permitido, inclusive o Codex em sua interface gráfica. **Não é necessário escrever código nem abrir o terminal.**

**Arquivo inicial:** [`aula_12_trilhas.json`](../../dados/casa/aula_12_trilhas.json) (pacote sintético). Confira os documentos complementares listados abaixo.

## Enunciado

**Dados.** Pacote novo com 16 rastros de execução de um agente fictício, oito decisões de aprovação humana e seis tentativas adversariais em documentos e mensagens.

**Questões de interpretação.**

1.  Classifique cada rastro por sucesso de tarefa e conformidade de trajetória.

2.  Localize pelo menos duas violações de fronteira de confiança.

3.  Verifique se aprovações e idempotência impediram ações indevidas.

4.  Calcule uma métrica de confiabilidade e explique suas hipóteses.

**Depósito no GitHub.** `auditoria.md`, `classificacao.csv`, `testes.json` e proposta de correção documentada. Todos os artefatos serão preparados ou revisados via interface gráfica, sem comandos de terminal.

**Quiz / fechamento.** Sem quiz subsequente; a atividade encerra o projeto e fornece casos para revisão conceitual da PF.

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

- [`aula_12_aprovacoes.csv`](../../dados/casa/aula_12_aprovacoes.csv)
- [`aula_12_ataques.md`](../../dados/casa/aula_12_ataques.md)
- [`aula_12_trilhas.json`](../../dados/casa/aula_12_trilhas.json)
