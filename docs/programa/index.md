# Programa da disciplina

## Objetivos

Ao final, o estudante deverá ser capaz de **formular** problemas de uso de IA, **distinguir** classificação, regressão, geração e recuperação de informações, **construir** aplicações assistidas por LLMs com fontes verificáveis, **selecionar** métricas adequadas, **utilizar** ferramentas externas e **avaliar** limites de agentes.

A construção matemática completa dos métodos não é pré-requisito. São exigidas interpretação quantitativa, comparação de alternativas e capacidade de explicar erros.

## Público e pré-requisitos

Estudantes do quarto semestre de Economia e Administração com estatística e inferência elementares, experiência básica com análise de dados e programação assistida. Conhecimentos avançados de Python, SQL, bancos de dados, contabilidade e macroeconomia não são pressupostos. Quando um método demanda uma ideia nova, a aula introduz a intuição mínima necessária.

## Encontros

| Aula | Tema | Área de aplicação | Evidência prática |
|---:|---|---|---|
| 01 | [O que um LLM faz — e o que não faz](../aulas/01-llms-e-limites/index.md) | Marketing | Ficha experimental de três respostas ao mesmo pedido, |
| 02 | [Embeddings, similaridade e concorrência](../aulas/02-embeddings-e-concorrencia/index.md) | Marketing | Mapa comparativo de produtos e teste de três consultas lexicais e semânticas. |
| 03 | [LLMs como componentes: extração estruturada](../aulas/03-saidas-estruturadas/index.md) | Finanças | Extrator de informações financeiras |
| 04 | [Classificação de mensagens e avaliação de LLMs](../aulas/04-classificacao-e-avaliacao/index.md) | Marketing | Relatório comparativo de dois prompts, baseline e tabela de erros. |
| 05 | [Ferramentas: quando o LLM deve calcular](../aulas/05-ferramentas-e-calculos/index.md) | Marketing e Finanças | Calculadora financeira e de campanhas acionada por perguntas em linguagem natural. |
| 06 | [Aplicações compostas: carteiras e indicadores](../aulas/06-aplicacoes-compostas/index.md) | Finanças e Macroeconomia | Miniaplicação que calcula retornos, volatilidades e produz síntese |
| 07 | [RAG: documentos como fonte de evidência](../aulas/07-rag-documentos/index.md) | Finanças | Protótipo de RAG sobre documentos fictícios |
| 08 | [Laboratório RAG: relatórios e política monetária](../aulas/08-rag-copom-relatorios/index.md) | Finanças e Macroeconomia | Assistente documental que responde a oito perguntas de teste, inclusive duas sem resposta no corpus. |
| 09 | [Avaliar RAG: recuperar e responder](../aulas/09-avaliacao-rag/index.md) | Marketing e Finanças | Relatório de avaliação |
| 10 | [Melhorar RAG sem perder rigor](../aulas/10-melhorar-rag/index.md) | Macroeconomia e Finanças | Comparação controlada de três variantes de RAG |
| 11 | [Agentes, ferramentas e fluxos de decisão](../aulas/11-agentes-e-workflows/index.md) | Macroeconomia | Agente limitado que seleciona consultar_série, calcular e buscar_documento; registra cada passo. |
| 12 | [Confiabilidade, avaliação e segurança de agentes](../aulas/12-confiabilidade-e-seguranca/index.md) | Marketing, Finanças e Macroeconomia | Relatório final de segurança |

Entre as aulas 6 e 7: **PI**. Após a aula 12: **PF**. Total: 14 encontros de duas horas.

## Regra para os casos

**Simples, sem serem simplórios.** Os casos devem conter uma pergunta que vale a pena responder, pelo menos um procedimento reproduzível e uma limitação intelectualmente relevante. O método será apresentado na profundidade necessária à interpretação, não à demonstração formal de todas as suas propriedades.

## Metodologia

- Início: formular a questão e explicitar o que seria um resultado aceitável.
- Núcleo conceitual: explicação concisa com pequenas contas e comparação de métodos.
- Simulador: prever o resultado antes de alterar os parâmetros; depois verificar.
- Notebook: executar, modificar uma hipótese e comparar resultados.
- Fecho: uma síntese individual com fonte, período, unidade e limitações.
- Semana: exercício comum individual documentado no Blackboard; sem atribuição de nota direta ao artefato.

## Avaliação

Nota = **20% quizzes + 35% PI + 45% PF** (proposta inicial a validar com a coordenação). Haverá 11 quizzes, no início das aulas 2 a 12. Sugestão: computar os **9 melhores** (descartar os dois menores), respeitando as regras institucionais de presença e avaliação. Cada quiz possui cinco questões objetivas ou numéricas com correção automática. PI e PF são individuais; questões conceituais exigem justificar decisões, detectar erros e interpretar saídas, sem avaliar memorização de sintaxe.

A aplicação via Blackboard e eventual proctoring via Smowl **depende de configuração e homologação institucional**; não há garantia técnica de prevenção de fraude. O professor deve testar o fluxo antes da primeira aula.

## Ferramentas

Python, pandas, NumPy e scikit-learn para exemplos reproduzíveis; Pydantic para validação; funções locais para ferramentas; LangChain, Chroma e LangGraph como implementações opcionais dos conceitos de RAG e agentes. O uso de qualquer fornecedor de LLM depende de chave própria e de regras institucionais. O percurso principal é funcional **sem API**.

## Leituras

1. Chip Huyen, *AI Engineering* (2025), seleção de capítulos sobre avaliação, RAG e agentes.
2. Andrea De Mauro, *Grokking AI Applications* (2025), casos e construção de aplicações.
3. Immanuel Trummer, *Data Analysis with LLMs* (2025), leitura orientada sobre análise de dados com LLMs.
4. Jay Alammar e Maarten Grootendorst, *An Illustrated Guide to AI Agents*, tópicos selecionados sobre arquiteturas e avaliação.
5. Pedro Fernandez e Paulo Marques, *Data Science, Marketing & Business*, referência para a **natureza dos problemas**, não para uma exigência de programação manual.

O material do curso é autossuficiente para os conceitos cobrados; as referências oferecem aprofundamento.
