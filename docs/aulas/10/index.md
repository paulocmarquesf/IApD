# Avaliação experimental de aplicações de IA

<span class="eyebrow">Aula 10 · Operações empresariais</span>

> **Propósito:** Uma mudança realmente melhorou o sistema, ou apenas produziu exemplos mais convincentes?

**Organização do encontro:** 15 minutos de quiz inicial (aulas 2 a 12); 45 minutos de conceitos e exercícios; 60 minutos de laboratório. A Aula 1 reserva 60 minutos para conceitos e 60 para o laboratório, sem quiz prévio.

**Objetivos:** Planejar comparações controladas, registrar ganhos e regressões, e avaliar respostas fundamentadas, custo e latência.

## Fundamentação conceitual

### 1. Comparações controladas

Melhorar uma aplicação exige definir o que será mantido constante, o que será modificado e qual métrica representará o objetivo. Uma avaliação antes/depois usando conjuntos de teste diferentes não identifica o efeito da mudança. O desenho mínimo usa uma configuração de referência (*baseline*) e uma alternativa, ambas aplicadas às mesmas entradas.

Para uma métrica $m$ calculada em $n$ exemplos, escrevemos a diferença emparelhada $\Delta=m_B-m_A$. Ao comparar resultados individuais, o vetor $d_i=s_i(B)-s_i(A)$ ajuda a examinar casos em que a nova configuração melhorou ou piorou. Uma média positiva pode esconder perdas graves em perguntas de risco elevado.

### 2. Separação de desenvolvimento e teste

É inadequado testar dezenas de prompts no mesmo conjunto e apresentar o maior escore como resultado independente: a escolha foi feita usando o teste. O desenho deve ter casos para especificação, casos para desenvolvimento e um conjunto final reservado. O mesmo cuidado se aplica à seleção de tamanho de chunk, top-k e limiares.

Um avaliador por LLM (*LLM-as-a-Judge*) pode atribuir notas ou comparar respostas, mas sua saída é uma medição potencialmente enviesada e variável. Devemos registrar o critério, fornecer evidência aos avaliadores, analisar discordâncias e manter casos de revisão humana. O juiz não deve ser a única fonte do gabarito.

### 3. Resultados e trade-offs

Uma versão que passa de 80% para 84% de acerto melhora quatro pontos percentuais, não quatro por cento relativos: a melhoria relativa é $(0{,}84-0{,}80)/0{,}80=5\%$. A clareza sobre denominadores é essencial. Em sistemas reais, desempenho também envolve tempo de resposta, custo de execução, taxa de abstenção e consumo de contexto. Não é correto comparar apenas qualidade sem considerar viabilidade operacional.

### 4. Diagnóstico por etapas

Para um RAG de atendimento, se a política correta não foi recuperada, testar o índice e a consulta; se foi recuperada mas a resposta contradiz a política, investigar geração e instruções; se a resposta está correta mas viola exigência de aprovação, investigar o workflow. O experimento deve registrar *qual etapa mudou* e *qual etapa falhou*. Assim, a aula transforma a ideia vaga de «melhorar o chatbot» em um procedimento de avaliação reprodutível.

## Exemplo de discussão para resolução manual

<div class="tcolorbox">

Em 20 solicitações, a baseline resolve corretamente 14 e a variante resolve 17. A taxa passa de 70% a 85%, ganho de 15 pontos percentuais. Se a variante corrige cinco casos antes errados e piora dois casos antes corretos, o ganho líquido é três. O estudante deve listar os dois casos de regressão, explicar por que só a diferença agregada é insuficiente e propor um critério que torne inaceitável determinada regressão de segurança.

</div>

## Laboratório: aplicação e verificação

**Dados da aula:** [`casos.csv`](../../dados/aula/aula_10/casos.csv), [`politicas.md`](../../dados/aula/aula_10/politicas.md), [`previsoes_A.csv`](../../dados/aula/aula_10/previsoes_A.csv), [`previsoes_B.csv`](../../dados/aula/aula_10/previsoes_B.csv). **Todos são didáticos/sintéticos.**

### Problema de decisão e dados disponibilizados

**Situação.** Uma equipe quer saber se acrescentar recuperação de políticas ao classificador de atendimento melhora a fundamentação sem introduzir regressões ou latência excessiva.

**Pacote de dados.** Versão docente limpa da triagem; `politicas.md` com regras fictícias datadas; `casos.csv` com 40 solicitações e rótulos. Previsões congeladas das configurações A (sem RAG) e B (com RAG) garantem comparação sem depender de novas chamadas de LLM.

### Laboratório em aula (60 minutos)

1.  Definir previamente desfecho primário, rubrica de citação e limite operacional de latência.

2.  Solicitar ao Codex comparação pareada, matriz de transições acerto–erro e relatórios de melhorias/regressões por ID.

3.  Inspecionar casos de documento desatualizado, regra de exceção e afirmação elegante sem evidência.

4.  Concluir se a mudança deve ser adotada, diferenciando ganho médio e risco de erro raro e grave.

### Especificação inicial por prompt

> **Compare duas configurações de triagem sobre os mesmos 40 casos. Calcule métricas pareadas, melhorias, regressões, fundamentação e tempos registrados, com relatórios por ID. Use previsões congeladas para que o experimento funcione sem chamada de modelo; não altere simultaneamente os dados.**

### Critérios de aceitação

Mesmos IDs e rótulos nas duas condições; regressões identificadas individualmente; latência descrita por mediana e quantis, se fornecidos; nenhuma inferência causal atribuída a mudanças múltiplas.

### Articulação com as demais aulas

O sistema de atendimento deixa de apenas recomendar respostas e passa a executar um fluxo operacional explicitamente modelado nas Aulas 11 e 12.

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

O quiz oficial de 15 minutos no início da aula cobre os conceitos da Aula 9 e a atividade correspondente, condicionada ao depósito no GitHub. As questões oficiais e o gabarito são reservados ao professor.

[Questões formativas de treinamento](../../apoio/treino.md#aula-10) (não são as questões da avaliação oficial).

## Referências para aprofundamento

Consulte a [bibliografia da disciplina](../../apoio/bibliografia.md) e as fontes técnicas indicadas no material específico.
