# Aula 11 — Exercícios conceituais

**Resolução individual em papel.** Mostre as contas intermediárias e explicite as hipóteses.

### Exercício 11.1 O sétimo dia

Uma regra didática permite devolução até 7 dias corridos após a entrega, incluindo o próprio sétimo dia. Classifique pedidos recebidos há 6, 7 e 8 dias; formule a guarda booleana que decide elegibilidade.

### Exercício 11.2 Um grafo com caminho proibido

Os estados são recebido, identificado, verificado, aprovado e concluído. O grafo admite aresta direta recebido $\to$ concluído. Qual controle falta? Descreva uma condição que impossibilite concluir sem identificar e verificar o pedido.

### Exercício 11.3 Escolher ou seguir uma regra?

Sistema X executa consultas em uma ordem fixa. Sistema Y escolhe entre duas ferramentas de leitura conforme os dados coletados. Explique que decisão é dinâmica em Y e por que isso não autoriza automaticamente operações de escrita.

### Exercício 11.4 O pedido não existe

A ferramenta de consulta retorna “pedido não encontrado” e o agente deduz uma entrega ontem para seguir o fluxo. Identifique a primeira transição inválida. Proponha um estado explícito de exceção e uma condição de parada.

### Exercício 11.5 Idempotência numa atualização

Uma ação `registrar_troca` é chamada três vezes para o mesmo pedido com o mesmo identificador de operação. Quantos registros de troca devem ser criados se o comando é idempotente? Qual identificador o sistema deve persistir para garantir esse comportamento?

### Exercício 11.6 Leia o rastro, não a justificativa

Um log registra recebido $\to$ verificado $\to$ concluído, com consulta a estoque bem-sucedida, mas nenhuma consulta de política de elegibilidade. O agente declara “todos os controles foram aplicados”. Que informação do log contradiz a declaração?

### Exercício 11.7: Transição de estado

Pedido entregue há 9 dias, regra didática 7 dias. Desenhe a transição e justifique o encaminhamento humano.

### Exercício 11.8: Idempotência

Uma requisição de estorno chega duas vezes com o mesmo ID. Quantos estornos são autorizados e que log deve existir?

### Exercício 11.9: Sem dados

Uma ferramenta retorna data_entrega=null. Qual caminho o workflow deve seguir?

### Exercício 11.10: Condição de parada

Um agente insiste em consultar o mesmo documento cinco vezes sem alterar a consulta. Especifique limite verificável.
