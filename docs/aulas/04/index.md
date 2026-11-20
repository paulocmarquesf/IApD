# Avaliação de aplicações com LLMs

<span class="eyebrow">Aula 04 · Operações empresariais</span>

> **Propósito:** Como medir se a triagem automatizada é útil quando os erros têm consequências diferentes?

**Organização do encontro:** 15 minutos de quiz inicial (aulas 2 a 12); 45 minutos de conceitos e exercícios; 60 minutos de laboratório. A Aula 1 reserva 60 minutos para conceitos e 60 para o laboratório, sem quiz prévio.

**Objetivos:** Construir um protocolo de avaliação com rótulos de referência, métricas de classificação, tipologia de falhas e comparação de prompts.

## Fundamentação conceitual

### 1. O que significa avaliar uma aplicação

O desempenho de uma triagem depende da definição de verdade de referência, da distribuição das mensagens e do custo dos erros. Um *golden set* é um conjunto cuidadosamente anotado, com regras de rotulagem e critérios de resolução de discordâncias. Não basta gerar rótulos automaticamente e tratá-los como verdade. O conjunto usado para aperfeiçoar prompts não deve ser o único conjunto usado para afirmar desempenho final: múltiplas escolhas sobre os mesmos dados geram sobreajuste à avaliação.

Para uma classe de interesse, a matriz de confusão contém verdadeiros positivos ($\text{TP}$), falsos positivos ($\text{FP}$), falsos negativos ($\text{FN}$) e verdadeiros negativos ($\text{TN}$). Essa matriz é definida sempre em relação a um rótulo positivo declarado.

$$
\text{Precision}=\frac{\text{TP}}{\text{TP}+\text{FP}},\qquad
\text{Recall}=\frac{\text{TP}}{\text{TP}+\text{FN}},
$$

$$
\text{Accuracy}=\frac{\text{TP}+\text{TN}}{\text{TP}+\text{FP}+\text{FN}+\text{TN}},\qquad
F_1=\frac{2\text{Precision}\,\text{Recall}}{\text{Precision}+\text{Recall}}.
$$

Essas medidas não capturam sozinhas o custo empresarial dos erros.

### 2. Exemplo resolvido: prioridades de atendimento

Em 50 mensagens, admita $\text{TP}=8$, $\text{FP}=4$, $\text{FN}=12$ e $\text{TN}=26$. Então $\text{Precision}=8/12\approx0{,}667$, $\text{Recall}=8/20=0{,}40$ e $\text{Accuracy}=34/50=0{,}68$. A aplicação deixa de identificar 60% das mensagens realmente urgentes, apesar da maioria das decisões estar correta. Um gestor que observa só a accuracy pode tomar uma decisão inadequada.

Se o custo de uma falsa urgência for 1 e o custo de deixar de identificar uma urgência for 5, a perda total será $L=1\text{FP}+5\text{FN}$. A escolha entre classificadores pode mudar quando muda a relação de custos. É necessário explicitar o critério **antes** de selecionar o melhor sistema.

### 3. Estabilidade e diagnóstico

O conjunto deve incluir classes raras, mensagens incompletas, negações e casos com múltiplos temas. Reportar apenas a média pode esconder falhas relevantes por subgrupo. Ao comparar versões, usar as mesmas entradas e controlar mudanças de taxonomia e pré-processamento. Para saídas estocásticas, replicar execuções e registrar variabilidade; uma única resposta não sustenta a afirmação de melhoria estável.

Erros de sintaxe, de classificação e de recuperação de informação são falhas diferentes. O diagnóstico deve apontar onde o processo falhou, com casos concretos e possíveis correções. Na avaliação de rótulos humanos, a discordância entre anotadores pode revelar ambiguidade real, em vez de simples defeito do prompt.

## Exemplo de discussão para resolução manual

<div class="tcolorbox">

Para oito mensagens, a classificação ’urgente’ apresenta $\text{TP}=3$, $\text{FP}=1$, $\text{FN}=2$ e $\text{TN}=2$. Calcular $\operatorname{Precision}=3/4=0{,}75$, $\operatorname{Recall}=3/5=0{,}60$ e $\operatorname{Accuracy}=(3+2)/8=0{,}625$. Se a perda por falso negativo é cinco vezes a perda por falso positivo, o custo relativo é $2\cdot5+1\cdot1=11$. Discutir como a política de encaminhamento mudaria se o custo de um falso negativo aumentasse.

</div>

## Laboratório: aplicação e verificação

**Dados da aula:** [`previsoes-a.csv`](../../dados/aula/aula_04/previsoes-a.csv), [`previsoes-b.csv`](../../dados/aula/aula_04/previsoes-b.csv), [`rotulos.csv`](../../dados/aula/aula_04/rotulos.csv). **Todos são didáticos/sintéticos.**

### Problema de decisão e dados disponibilizados

**Situação.** Uma central recebe reclamações potencialmente urgentes e deseja avaliar se a triagem automática reduz riscos sem sobrecarregar a equipe humana. Os erros têm consequências diferentes.

**Pacote de dados.** `rotulos.csv`: 60 solicitações fictícias com rótulo humano de urgência e justificativa; `previsoes-a.csv` e `previsoes-b.csv`: saídas de duas configurações congeladas, para comparar mesmo se o SDK não estiver disponível.

### Laboratório em aula (60 minutos)

1.  Definir positivo como “urgente” e construir uma matriz de confusão de seis casos exemplares à mão.

2.  Pedir ao Codex um painel comparativo das duas configurações, com matriz, precision, recall, custo assimétrico e lista de discordâncias.

3.  Inspecionar cinco falsos negativos e distinguir erro de referência, erro de leitura da mensagem e erro de regra.

4.  Escolher uma configuração sob dois cenários de custo, justificando por que accuracy isolada é insuficiente.

### Especificação inicial por prompt

> **Construa um avaliador local que receba rótulos humanos e duas tabelas de previsões fixas por ID, calcule as métricas e mostre casos de erro. Implemente também comparação do custo com FN cinco vezes mais caro que FP, sem exigir qualquer chamada de modelo.**

### Critérios de aceitação

Matrizes somam 60 casos; IDs pareados sem duplicação; denominadores apresentados; casos de rótulos controversos sinalizados; custo calculado com a convenção declarada.

### Articulação com as demais aulas

Os limites da classificação por linguagem motivam integrar funções confiáveis para cálculo e consulta a dados na Aula 5.

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

O quiz oficial de 15 minutos no início da aula cobre os conceitos da Aula 3 e a atividade correspondente, condicionada ao depósito no GitHub. As questões oficiais e o gabarito são reservados ao professor.

[Questões formativas de treinamento](../../apoio/treino.md#aula-04) (não são as questões da avaliação oficial).

## Referências para aprofundamento

Consulte a [bibliografia da disciplina](../../apoio/bibliografia.md) e as fontes técnicas indicadas no material específico.


## Simulação interativa

[Experimentar os parâmetros numéricos](../../assets/simuladores/index.html). A simulação complementa, mas não substitui, os cálculos feitos em papel.
