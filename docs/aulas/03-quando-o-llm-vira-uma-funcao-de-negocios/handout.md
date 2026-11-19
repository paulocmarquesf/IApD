# Handout 03 · Quando o LLM vira uma função de negócios

**Insper · Inteligência Artificial para Decisão**  
**Docente:** Paulo C. Marques F.  
**Entrega:** início do próximo encontro, salvo o handout final, entregue ao término do curso.

## Problema

Receba mensagens de uma empresa de serviços, não de varejo, e faça o Codex construir a versão de triagem com esquema adaptado a esse setor.

## Produto solicitado

Uma aplicação funcional construída inteiramente por prompts no Codex, acompanhada de uma nota analítica de até uma página. É permitido utilizar a rota API ou Codex CLI/SDK, desde que o modo de execução seja identificado. A demonstração determinística deve continuar executável sem credenciais.

## Requisitos mínimos

1. Identificar a origem de cada conjunto de dados utilizado.
2. Registrar ao menos três casos de teste com suas entradas e saídas.
3. Explicar o mecanismo central trabalhado na aula.
4. Identificar uma limitação concreta da implementação.
5. Guardar o prompt final, os resultados e os critérios de verificação.

## Perguntas orientadoras

**Pergunta principal:** Em qual caso a saída passou na validação do esquema e mesmo assim interpretou mal a solicitação?

**Pergunta conceitual:** Classifique uma lista de registros em três classes: JSON inválido, JSON válido com campos incorretos, JSON válido e coerente.

**Pergunta de avaliação:** Em que circunstância a aplicação deveria indicar que não possui evidência suficiente?

## Critérios de correção

Clareza do problema (20%); correspondência entre especificação e implementação (25%); testes e evidências (35%); interpretação dos limites (20%). Não são atribuídos pontos pela digitação manual de código.

## Dados e reprodutibilidade

As bases didáticas encontram-se na pasta `dados/`. A origem sintética deve permanecer registrada. Quando forem utilizadas fontes públicas, anotar endereço e data de consulta.
