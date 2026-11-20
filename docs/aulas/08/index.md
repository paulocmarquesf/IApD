# Sistemas conversacionais (chatbots)

<span class="eyebrow">Aula 08 · Finanças</span>

> **Propósito:** Como responder uma pergunta de acompanhamento sem perder a entidade e o período discutidos anteriormente?

**Organização do encontro:** 15 minutos de quiz inicial (aulas 2 a 12); 45 minutos de conceitos e exercícios; 60 minutos de laboratório. A Aula 1 reserva 60 minutos para conceitos e 60 para o laboratório, sem quiz prévio.

**Objetivos:** Projetar chatbots documentais com histórico, resolução de referências, recuperação contextual e abstenção fundamentada.

## Fundamentação conceitual

### 1. Conversa como estado

Um chatbot documental recebe uma sequência de turnos. A pergunta atual pode depender de referentes introduzidos anteriormente: «Qual é a taxa do Fundo A?» seguida de «E a liquidez dele?». A segunda pergunta não é autossuficiente. A consulta reescrita deve incorporar o fundo correto, a classe pertinente e a versão do documento, sem acrescentar informações que o usuário não deu.

Podemos representar o estado conversacional por $S_t$ e a transformação de consulta por

$$
q'_t=\operatorname{rewrite}(q_t,S_{t-1}).
$$

A consulta $q'_t$ é submetida ao retriever. A resposta deve permanecer vinculada aos trechos retornados e não apenas ao estado narrativo da conversa. O histórico ajuda a identificar a pergunta; ele não confirma dados financeiros.

### 2. Referência, ambiguidade e abstenção

Imagine que o diálogo alternou entre Fundos A e B e o usuário pergunta «Qual deles tem resgate mais rápido?». Aqui uma comparação é apropriada, mas pode exigir documentos e classes diferentes. Já «Qual o prazo dele?» após discutir duas classes sem especificação não possui referente inequívoco. O chatbot deve solicitar esclarecimento.

O conteúdo deve distinguir taxa de administração, taxa de performance, cotização, liquidação e prazo de resgate. Uma resposta correta para uma classe pode ser incorreta para outra. O campo temporal também é essencial: regulamentos e lâminas são documentos versionados.

### 3. Fluxo de um chatbot RAG

A aplicação executa recepção da pergunta, atualização de estado, reformulação, recuperação, verificação documental, geração e exibição de fontes. Para cada pergunta, o laboratório deve permitir inspecionar **qual consulta foi realmente recuperada**. A falha pode nascer na resolução da referência, antes de qualquer busca.

Um conjunto de testes deve conter turnos independentes, dependentes do histórico, mudanças explícitas de fundo, mudanças implícitas, perguntas sem documento suficiente e perguntas que exigem abstenção. A avaliação deve separar correção da consulta reescrita, recuperação de fontes e fundamentação da resposta final.

### 4. Documentação e responsabilidade

Os documentos didáticos de fundos de investimento serão fictícios, evitando confusão com produtos reais. A aplicação será um assistente de consulta a documentos, e não um consultor de investimentos. Ao usuário deverá ser mostrado o trecho e sua versão, inclusive quando o sistema não consegue responder. O Codex Python SDK poderá integrar a geração, sujeito à validação institucional; a recuperação deve funcionar independentemente do LLM.

## Exemplo de discussão para resolução manual

<div class="tcolorbox">

Turno 1: "Qual é a taxa de administração do Fundo A no regulamento de março?". Turno 2: "E a liquidez dele?". O estudante deve reformular o segundo turno como "Qual é a regra de liquidez do Fundo A no documento de março?" e explicar por que buscar apenas "liquidez" no corpus pode recuperar o Fundo B. Um trecho do Fundo B que menciona D+1 é lexicalmente relevante, mas documentalmente incorreto para a pergunta.

</div>

## Laboratório: aplicação e verificação

**Dados da aula:** [`delta.md`](../../dados/aula/aula_08/delta.md), [`dialogos.csv`](../../dados/aula/aula_08/dialogos.csv), [`horizonte.md`](../../dados/aula/aula_08/horizonte.md), [`omega.md`](../../dados/aula/aula_08/omega.md). **Todos são didáticos/sintéticos.**

### Problema de decisão e dados disponibilizados

**Situação.** Um assistente documental deve responder perguntas sucessivas sobre fundos de investimento, resolvendo pronomes, classes e datas, mas sem completar números não presentes nos documentos.

**Pacote de dados.** Documentos didáticos fictícios de três fundos de investimento (regulamento, lâmina e resumo de taxas), com versões e classes diferenciadas; `dialogos.csv` com seis conversas de dois a quatro turnos e perguntas ambíguas.

### Laboratório em aula (60 minutos)

1.  Reformular manualmente três perguntas dependentes do histórico, explicitando fundo, classe e data.

2.  Pedir ao Codex interface gráfica de chatbot com histórico, reformulação da consulta, recuperação documental local e citações por resposta.

3.  Inspecionar um diálogo em que “ele” se refere ao fundo anterior e outro que alterna dois fundos.

4.  Forçar documento inexistente e versão desatualizada; verificar pedido de esclarecimento e abstenção.

### Especificação inicial por prompt

> **Crie um chatbot local para documentos didáticos de três fundos de investimento. Preserve histórico e mostre a consulta reformulada, filtros de fundo/classe/data, trechos recuperados e citações. Respostas sem fonte devem declarar insuficiência; use o Codex SDK somente quando a integração estiver validada.**

### Critérios de aceitação

Referentes corretos em diálogos com alternância de fundos; números citados na classe/data correspondente; pedido de esclarecimento para identidade incerta; consultas e fontes recuperadas observáveis.

### Articulação com as demais aulas

A Aula 9 avalia quantitativamente o estágio de recuperação, independentemente da qualidade superficial do texto produzido pelo chatbot.

### Roteiro de verificação com o Codex

1. Examine a base de referência e registre a origem, as colunas e a unidade de análise.
2. Na **interface gráfica do Codex**, descreva a aplicação, as entradas, as saídas e os critérios de aceitação; solicite que o agente crie os arquivos.
3. Peça ao Codex que execute os testes, mostre os resultados e explique qualquer falha encontrada. O aluno não escreve código nem usa terminal.
4. Compare pelo menos um resultado com um cálculo ou verificação manual realizado em sala.
5. Registre dois casos em que a aplicação deveria se abster, solicitar esclarecimento ou sinalizar uma limitação.

**Material complementar:** [slides da aula (PDF)](slides.pdf) · [fonte LaTeX](slides.tex) · [exercícios no papel](exercicios.md) · [atividade para casa](casa.md).

## Exercícios e preparação da prova

Os dez problemas desta aula estão reunidos no [caderno de exercícios](exercicios.md). Os alunos devem explicitar as contas e justificar as conclusões. A escrita manual de código não é parte das avaliações.

## Verificação da aprendizagem

O quiz oficial de 15 minutos no início da aula cobre os conceitos da Aula 7 e a atividade correspondente, condicionada ao depósito no GitHub. As questões oficiais e o gabarito são reservados ao professor.

[Questões formativas de treinamento](../../apoio/treino.md#aula-08) (não são as questões da avaliação oficial).

## Referências para aprofundamento

Consulte a [bibliografia da disciplina](../../apoio/bibliografia.md) e as fontes técnicas indicadas no material específico.


**Nota sobre o corpus:** os fundos, classes, taxas e documentos são fictícios. O objetivo é comparar versões e classes documentais em um ambiente reproduzível.
