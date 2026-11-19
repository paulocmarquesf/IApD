# Handout 01 · Como uma máquina produz linguagem?

**Insper · Inteligência Artificial para Decisão**  
**Docente:** Paulo C. Marques F.  
**Entrega:** início do próximo encontro, salvo o handout final, entregue ao término do curso.

## Problema

Receba um segundo conjunto de avaliações de uma categoria de produto distinta. Construa, exclusivamente por prompts ao Codex, a mesma análise, mas com campos explícitos de evidência e de informação não encontrada.

## Produto solicitado

Uma aplicação funcional construída inteiramente por prompts no Codex, acompanhada de uma nota analítica de até uma página. É permitido utilizar a rota API ou Codex CLI/SDK, desde que o modo de execução seja identificado. A demonstração determinística deve continuar executável sem credenciais.

## Requisitos mínimos

1. Identificar a origem de cada conjunto de dados utilizado.
2. Registrar ao menos três casos de teste com suas entradas e saídas.
3. Explicar o mecanismo central trabalhado na aula.
4. Identificar uma limitação concreta da implementação.
5. Guardar o prompt final, os resultados e os critérios de verificação.

## Perguntas orientadoras

**Pergunta principal:** Em quais mensagens a conclusão do sistema depende de uma informação não presente no texto?

**Pergunta conceitual:** Compare a geração gulosa e a amostragem em uma tabela de três probabilidades e explique por que saídas diferentes não provam que uma está errada.

**Pergunta de avaliação:** Em que circunstância a aplicação deveria indicar que não possui evidência suficiente?

## Critérios de correção

Clareza do problema (20%); correspondência entre especificação e implementação (25%); testes e evidências (35%); interpretação dos limites (20%). Não são atribuídos pontos pela digitação manual de código.

## Dados e reprodutibilidade

As bases didáticas encontram-se na pasta `dados/`. A origem sintética deve permanecer registrada. Quando forem utilizadas fontes públicas, anotar endereço e data de consulta.
