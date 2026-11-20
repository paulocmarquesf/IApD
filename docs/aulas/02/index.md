# Embeddings e similaridade semântica

<span class="eyebrow">Aula 02 · Marketing Analítico</span>

> **Propósito:** Como transformar textos em representações comparáveis sem confundir proximidade semântica com identidade de consumidores?

**Organização do encontro:** 15 minutos de quiz inicial (aulas 2 a 12); 45 minutos de conceitos e exercícios; 60 minutos de laboratório. A Aula 1 reserva 60 minutos para conceitos e 60 para o laboratório, sem quiz prévio.

**Objetivos:** Interpretar embeddings, medidas de similaridade e agrupamentos exploratórios, produzindo uma análise replicável de avaliações e marcas.

## Fundamentação conceitual

### 1. Representação vetorial de textos

Um modelo de *embeddings* associa a cada texto $s$ um vetor $e(s)\in\mathbb R^d$. A representação é aprendida e depende do modelo, do idioma e do pré-processamento. Não se deve assumir que cada coordenada represente diretamente um atributo de mercado. Vetores são instrumentos para comparar descrições, mas a relação entre semântica e geometria não é perfeita: sinônimos, ironia, negação e mudança de domínio podem alterar as distâncias.

No caso de avaliações, é necessário definir a **unidade estatística**. Um comentário, uma avaliação e um cliente não são a mesma observação. Um consumidor prolífico pode produzir dezenas de textos e dominar a distribuição dos comentários; isso não implica que domine a distribuição dos consumidores. Para segmentação de clientes, precisamos de identificadores, critérios de agregação e amostragem apropriada.

### 2. Produto interno, norma e similaridade

Para vetores não nulos $u,v\in\mathbb R^d$, definimos

$$
\langle u,v\rangle=\sum_{j=1}^d u_jv_j,\qquad
\|u\|_2=\sqrt{\sum_{j=1}^d u_j^2},\qquad
\cos(u,v)=\frac{\langle u,v\rangle}{\|u\|_2\|v\|_2}.
$$

A similaridade cosseno pertence ao intervalo $[-1,1]$ para vetores reais não nulos. Ela é invariável a multiplicação por constante positiva: $\cos(u,3u)=1$. Já a distância euclidiana entre $u$ e $3u$ é $2\|u\|$. Portanto, alinhamento não significa proximidade absoluta nem intensidade idêntica.

**Exemplo resolvido.** Para $u=(1,0)$, $v=(3,4)$ e $w=(-2,0)$, temos $\cos(u,v)=3/5$, $\cos(u,w)=-1$ e $\|u-v\|_2=\sqrt{20}$. A diferença entre a ordenação por cosseno e por distância deve ser explicitada antes de interpretar um gráfico.

### 3. Agregação, agrupamentos e projeção

O centroide de $m$ vetores é $\bar e=m^{-1}\sum_{i=1}^m e_i$. Ele minimiza a soma das distâncias euclidianas quadráticas dentro de um grupo, mas pode ser distorcido por observações extremas. Um algoritmo de agrupamento é exploratório: a existência de dois clusters numéricos não prova a existência de dois segmentos comerciais. É indispensável examinar estabilidade, conteúdo dos grupos e composição dos dados.

Projetar embeddings para duas dimensões pode facilitar a inspeção, mas sempre requer atenção à distorção. Se a distância original satisfaz $d(A,B)<d(A,C)$ e a figura apresenta o contrário, o mapa não preservou nem a ordenação local desse trio. Para posicionamento de marcas, atributos, preços e participação de mercado devem provir de fontes próprias; não são inferíveis diretamente de uma nuvem de comentários.

### 4. Aplicação à decisão

Na análise de marcas, a pergunta relevante pode ser: «Quais atributos estão semanticamente associados às avaliações de cada marca, e com que incerteza?». A aplicação pode recuperar avaliações exemplares, calcular centroides e localizar observações discrepantes. Deve mostrar também quantas avaliações e quantos clientes geraram cada resultado, a distribuição de notas e casos discordantes. Um gráfico sem essas informações pode ter grande apelo visual e pequeno valor analítico.

## Exemplo de discussão para resolução manual

<div class="tcolorbox">

Considere $A=(1,0)$ e $B=(3,4)$. O produto interno é $3$, as normas são $1$ e $5$, e a similaridade cosseno é $0{,}6$. Para $C=(-1,0)$, a similaridade entre $A$ e $C$ é $-1$. Discutir por que $B$ pode ser mais distante em termos euclidianos e, ainda assim, relativamente alinhado com $A$. Em um conjunto de comentários, calcular também uma média vetorial simples de dois embeddings e interpretar suas limitações.

</div>

## Laboratório: aplicação e verificação

**Dados da aula:** [`dados.csv`](../../dados/aula/aula_02/dados.csv), [`vetores_ilustrativos.csv`](../../dados/aula/aula_02/vetores_ilustrativos.csv). **Todos são didáticos/sintéticos.**

### Problema de decisão e dados disponibilizados

**Situação.** Um fabricante deseja saber se as avaliações de quatro marcas de mochilas destacam atributos semelhantes. O objetivo é estudar a geometria da representação textual, distinguindo grupos de comentários de segmentos de clientes.

**Pacote de dados.** `dados.csv`: 48 avaliações sintéticas de quatro marcas, com `id`, `marca`, `texto` e `atributo-referencia` para oito frases demonstrativas. Modelo multilíngue local de embeddings disponibilizado previamente pelo professor, com versão registrada.

### Laboratório em aula (60 minutos)

1.  Comparar manualmente dois vetores bidimensionais e formular uma hipótese sobre uma frase próxima e outra distante.

2.  Pedir ao Codex embeddings locais, matriz de cossenos, recuperação dos três vizinhos e visualização exploratória com rótulo de marca.

3.  Testar cossenos para frases idênticas, matriz simétrica e casos de negação; comparar duas escolhas simples de agrupamento.

4.  Examinar dois grupos com textos literais e explicar por que uma projeção 2D não demonstra segmentação de pessoas.

### Especificação inicial por prompt

> **Construa um explorador local de embeddings para o conjunto de 48 avaliações. Mostre cossenos, vizinhos, grupos e textos originais; registre o modelo e parâmetros. Evite API convencional e não interprete grupos de comentários como perfis demográficos.**

### Critérios de aceitação

Cossenos simétricos e próximos de 1 na diagonal de vetores não nulos; modelo identificado; grupos acompanhados de exemplos; nenhuma afirmação sobre market share ou número de clientes sem denominador apropriado.

### Articulação com as demais aulas

A experiência com resultados textuais variáveis motiva a criação de contratos de saída, formatos estruturados e validações na Aula 3.

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

O quiz oficial de 15 minutos no início da aula cobre os conceitos da Aula 1 e a atividade correspondente, condicionada ao depósito no GitHub. As questões oficiais e o gabarito são reservados ao professor.

[Questões formativas de treinamento](../../apoio/treino.md#aula-02) (não são as questões da avaliação oficial).

## Referências para aprofundamento

Consulte a [bibliografia da disciplina](../../apoio/bibliografia.md) e as fontes técnicas indicadas no material específico.


## Simulação interativa

[Experimentar os parâmetros numéricos](../../assets/simuladores/index.html). A simulação complementa, mas não substitui, os cálculos feitos em papel.
