# Aula 08 — Exercícios conceituais

**Resolução individual em papel.** Mostre as contas intermediárias e explicite as hipóteses.

### Exercício 8.1 Quem é “ele”?

Histórico: “Qual o prazo de resgate do Fundo Norte?”; “E a taxa do Fundo Sul?”; “Ela é maior que a do primeiro?”. Identifique a referência de “ela” e de “primeiro”. Reescreva a terceira pergunta como consulta independente sem acrescentar informação.

### Exercício 8.2 Comparação sem documento

O usuário pede “Qual fundo tem menor taxa?”, mas o corpus contém a taxa do Fundo A e não contém documento do Fundo B. É adequado responder “A”? Proponha uma resposta com limitação explícita e a condição que permitiria uma comparação válida.

### Exercício 8.3 Memória curta, consequência longa

Um sistema conserva apenas os dois turnos anteriores. No turno 1, o usuário define a data de referência; no turno 4, pergunta “E nessa data?”. Mostre por que o sistema pode perder o referente e qual mecanismo de estado explícito poderia preservá-lo.

### Exercício 8.4 Documento de outra classe

Uma consulta é sobre taxa de administração de uma classe específica do Fundo A. O trecho recuperado refere-se a outra classe do mesmo fundo. Quais metadados precisam integrar o filtro? Que verificação o chatbot deve executar antes de citar o número?

### Exercício 8.5 Resposta com duas afirmações

Um chatbot diz “O fundo aplica em ações e permite resgate D+1”, citando um trecho que informa apenas a política de investimento. Quantas afirmações há? Classifique cada uma quanto à evidência e proponha uma resposta corrigida.

### Exercício 8.6 O que o chatbot deve perguntar

Um cliente pergunta “Quanto pago para sair do fundo?”, sem especificar fundo nem classe. Defina uma pergunta de esclarecimento mínima. Explique por que uma estimativa numérica inventada seria inadequada, mesmo que frequentemente existam taxas semelhantes no mercado.

### Exercício 8.7: Pronome ambíguo

Após comparar Fundos A e B, o usuário pergunta “Qual a taxa dele?”. O que deve fazer um chatbot fundamentado?

### Exercício 8.8: Histórico contraditório

O histórico afirma taxa de 1,2%, mas documento atualizado diz 1,1%. Qual informação tem prioridade e como citar?

### Exercício 8.9: Consulta reescrita

Transforme “E quando ele paga?” em pergunta autossuficiente após: “Vamos comparar o Fundo A, classe C, no regulamento de março”.

### Exercício 8.10: Versão e classe

A regra D+1 existe apenas na classe A; a pergunta é sobre a classe B. Como testar a resposta?
