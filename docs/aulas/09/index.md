# Avaliação da recuperação de informação

<span class="eyebrow">Aula 09 · Finanças</span>

> **Propósito:** O recuperador encontrou a informação certa e a colocou em uma posição útil do ranking?

**Organização do encontro:** 15 minutos de quiz inicial (aulas 2 a 12); 45 minutos de conceitos e exercícios; 60 minutos de laboratório. A Aula 1 reserva 60 minutos para conceitos e 60 para o laboratório, sem quiz prévio.

**Objetivos:** Calcular Hit@k e MRR, compreender os fundamentos de busca lexical e densa e executar comparações controladas em corpus documental.

## Fundamentação conceitual

### 1. Relevância e ranking

A recuperação de informação é uma tarefa de ordenação: dada uma consulta $q$, o sistema atribui escores aos documentos e produz um ranking. O desempenho depende dos **juízos de relevância**, não apenas da fluência do texto final. Um documento relevante pode ser deixado abaixo do corte top-k mesmo quando existe no corpus.

Se $R(q)$ é o conjunto de documentos relevantes e $T_k(q)$ o conjunto dos $k$ primeiros resultados, uma medida de cobertura é $\operatorname{Recall@}k=|R(q)\cap T_k(q)|/|R(q)|$. Em tarefas com uma evidência principal, Hit@k indica se ao menos uma evidência relevante aparece nos $k$ primeiros.

$$
\operatorname{Hit@}k(q)=\mathbf1\{R(q)\cap T_k(q)\ne\varnothing\},\qquad
\operatorname{RR}(q)=\frac1{r_q},
$$

em que $r_q$ é a posição da primeira evidência relevante (adotamos $\operatorname{RR}=0$ quando não existe no ranking). Para $m$ perguntas, $\operatorname{MRR}=m^{-1}\sum_{i=1}^m \operatorname{RR}(q_i)$.

### 2. Exemplo calculado

Em três consultas, o primeiro documento relevante aparece, respectivamente, nas posições 1, 4 e 2. A média das reciprocidades é

$$
\operatorname{MRR}=\frac{1+1/4+1/2}{3}=\frac{7}{12}\approx0{,}583.
$$

Já Hit@3 é $2/3$, pois a segunda pergunta não encontrou evidência entre os três primeiros. Relatar apenas Hit@3 esconderia a diferença entre posições 1 e 2; relatar apenas MRR não informaria quantas evidências relevantes foram recuperadas quando existem várias.

### 3. Recuperação lexical, densa e híbrida

TF-IDF atribui maior peso a termos frequentes no documento e pouco frequentes no acervo, com escolhas específicas de normalização. BM25 acrescenta controle de saturação e do comprimento documental. Uma formulação clássica é

$$
\operatorname{BM25}(q,d)=\sum_{t\in q}\operatorname{IDF}(t)
\frac{f(t,d)(k_1+1)}{f(t,d)+k_1(1-b+b|d|/\overline{|d|})}.
$$

As constantes $k_1$ e $b$ controlam saturação e normalização. Busca densa compara embeddings e pode recuperar paráfrases, mas não assegura melhor resultado para identificadores, taxas ou códigos específicos. Busca híbrida combina evidências de natureza distinta, exigindo uma regra de fusão.

### 4. Avaliar o componente certo

Os testes de recuperação devem ser executados **antes** de chamar o modelo gerador. É necessário criar um conjunto de consultas, guardar evidências esperadas, congelar o corpus e comparar rankings sob os mesmos parâmetros. Uma resposta bem redigida não é evidência de recuperação correta. Para os fundos de investimento, perguntas sobre taxas, classes e prazos devem possuir identificadores e versões documentais inequívocos.

## Exemplo de discussão para resolução manual

<div class="tcolorbox">

Três consultas têm o primeiro trecho relevante nas posições $2$, $1$ e fora do ranking recuperado. Os reciprocal ranks são $\frac12$, $1$ e $0$, de modo que $\mathrm{MRR}=\frac{1/2+1+0}{3}=0{,}5$. Para $k=3$, $\mathrm{Hit}@3=2/3$; para $k=1$, $\mathrm{Hit}@1=1/3$. Explicar por que respostas eloquentes não compensam uma recuperação deficiente.

</div>

## Laboratório: aplicação e verificação

**Dados da aula:** [`consultas.csv`](../../dados/aula/aula_09/consultas.csv), [`relevancia.csv`](../../dados/aula/aula_09/relevancia.csv), [`trechos.csv`](../../dados/aula/aula_09/trechos.csv). **Todos são didáticos/sintéticos.**

### Problema de decisão e dados disponibilizados

**Situação.** Uma biblioteca documental precisa comparar recuperação lexical, densa e híbrida antes de decidir qual sistema alimentará um chatbot. O interesse é localizar documentos relevantes, não julgar a fluência das respostas.

**Pacote de dados.** Starter do chatbot com 20 trechos de documentos de fundos de investimento e `consultas.csv` com 12 perguntas; `relevancia.csv` com pares consulta–trecho e rótulos de referência auditados.

### Laboratório em aula (60 minutos)

1.  Calcular à mão Hit@3 e MRR@3 para três rankings pequenos.

2.  Pedir ao Codex avaliador local de BM25, embeddings e fusão por postos, com mesmas consultas, corpus e rótulos.

3.  Construir relatório por consulta, não apenas médias; estudar caso lexical favorável e paráfrase favorável à busca densa.

4.  Comparar k=1,3,5, investigar empates e delimitar o que a avaliação de recuperação não diz sobre veracidade das respostas.

### Especificação inicial por prompt

> **Implemente, sobre corpus fixo, três recuperadores locais: BM25, embeddings e combinação por postos. Use rótulos de relevância fornecidos para calcular Hit@k e MRR@k; exiba resultados por pergunta, parâmetros e casos em que cada método falha.**

### Critérios de aceitação

Fórmulas e denominadores explícitos; método de desempate reproduzível; mesmas consultas para todos os modelos; zero para perguntas sem relevante nos k primeiros, com convenção declarada.

### Articulação com as demais aulas

As noções de baseline, ganho e regressão alimentarão a avaliação experimental de aplicações completas na Aula 10.

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

O quiz oficial de 15 minutos no início da aula cobre os conceitos da Aula 8 e a atividade correspondente, condicionada ao depósito no GitHub. As questões oficiais e o gabarito são reservados ao professor.

[Questões formativas de treinamento](../../apoio/treino.md#aula-09) (não são as questões da avaliação oficial).

## Referências para aprofundamento

Consulte a [bibliografia da disciplina](../../apoio/bibliografia.md) e as fontes técnicas indicadas no material específico.


## Simulação interativa

[Experimentar os parâmetros numéricos](../../assets/simuladores/index.html). A simulação complementa, mas não substitui, os cálculos feitos em papel.


**Nota sobre o corpus:** os fundos, classes, taxas e documentos são fictícios. O objetivo é comparar versões e classes documentais em um ambiente reproduzível.
