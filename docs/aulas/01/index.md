# Fundamentos dos Large Language Models

<span class="eyebrow">Aula 01 · Marketing Analítico</span>

> **Propósito:** O que um LLM faz ao produzir uma resposta e por que essa resposta não é, por si só, uma evidência?

**Organização do encontro:** 15 minutos de quiz inicial (aulas 2 a 12); 45 minutos de conceitos e exercícios; 60 minutos de laboratório. A Aula 1 reserva 60 minutos para conceitos e 60 para o laboratório, sem quiz prévio.

**Objetivos:** Compreender o mecanismo de geração de linguagem e distingui-lo de classificação, cálculo e consulta a bases de dados. Iniciar a prática de especificação e verificação de software por prompts no Codex (interface gráfica).

## Fundamentação conceitual

### 1. Linguagem como sequência de tokens

Um *Large Language Model* (LLM) autorregressivo recebe uma sequência de tokens e estima uma distribuição de probabilidade para o token seguinte. **Token não é sinônimo de palavra**: uma palavra pode ser representada por vários tokens, e sinais de pontuação, espaços e fragmentos frequentes podem ter representações próprias. Consequentemente, o custo de contexto depende da tokenização efetiva. O limite de contexto inclui instruções, histórico, documentos e a própria pergunta, e não apenas o texto visível da última mensagem.

Denotemos por $x_1,\ldots,x_n$ a sequência tokenizada. A regra da cadeia da probabilidade fornece

$$
P(x_1,\ldots,x_n)=\prod_{i=1}^{n}P(x_i\mid x_1,\ldots,x_{i-1}).
$$

Essa fatoração não afirma que o modelo consulta fatos externos; descreve o problema probabilístico que a modelagem resolve. O treinamento ajusta parâmetros a partir de sequências; na inferência, o modelo aplica os parâmetros já aprendidos a um contexto particular. A aplicação de negócios é uma terceira camada: especifica como converter textos em resultados que possam ser verificados.

### 2. Decodificação e variabilidade

Se os escores de três tokens forem $z_1,z_2,z_3$, a distribuição normalizada por *softmax* à temperatura $\tau>0$ é

$$
p_i=\frac{\exp(z_i/\tau)}{\sum_j\exp(z_j/\tau)}.
$$

A escolha *greedy* seleciona o maior $p_i$; a amostragem pode selecionar alternativas menos prováveis. Temperatura controla a dispersão da distribuição, não a veracidade. Temperatura reduzida não equivale a uma verificação de fontes. O exemplo da tabela separa probabilidade de correção factual.

| Próximo token | Probabilidade | Saída greedy | Possível na amostragem |
|:--|--:|:--:|:--:|
| mantido | 0,50 | Sim | Sim |
| ampliado | 0,35 | Não | Sim |
| revisto | 0,15 | Não | Sim |

A chance de a amostragem retornar uma alternativa a «mantido» é $0{,}35+0{,}15=0{,}50$. Isso pode ser calculado sem executar nenhum modelo.

### 3. Atenção como combinação condicionada ao contexto

No mecanismo de *scaled dot-product attention*, para uma matriz de representações $X\in\mathbb R^{n\times d}$, definimos $Q=XW_Q$, $K=XW_K$ e $V=XW_V$. Uma cabeça de atenção calcula

$$
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}+M\right)V,
$$

em que $M$ impede que uma posição causal acesse tokens futuros. O produto entre queries e keys produz escores de compatibilidade; os pesos após *softmax* combinam os valores. A operação não é uma busca na internet, e pesos de atenção elevados não constituem prova de influência causal. Em um exemplo escalar com escores não normalizados $3$ e $1$ e valores $4$ e $0$, os pesos são $3/4$ e $1/4$, de modo que a combinação é $3$.

### 4. Evidência, extração e inferência

Considere a avaliação «A embalagem chegou intacta, mas o produto falhou duas vezes». São sustentadas as afirmações sobre embalagem e falhas; não são sustentadas afirmações sobre fraude, reembolso ou intenção de recompra. Um painel de Marketing Analítico deve distinguir observação textual, classificação sugerida e inferência do analista. Uma citação literal verificável é mais forte do que uma descrição plausível sem rastreabilidade. Identificadores de registros permitem voltar à fonte; casos inconclusivos não devem ser convertidos artificialmente em categorias certas.

**Exemplo resolvido.** Uma janela comporta 16 tokens. Instruções consomem 5, documentos recuperados 6 e a pergunta 7. O total é 18; excede a janela em 2. Remover indiscriminadamente os dois tokens mais antigos pode eliminar uma negação ou referência. A solução deve preservar o significado, não apenas reduzir a contagem.

## Exemplo de discussão para resolução manual

<div class="tcolorbox">

Exemplo 1: diante das probabilidades 0,50, 0,30 e 0,20 para três próximos tokens, identificar a escolha mais provável e explicar por que uma geração pode escolher outro token. Exemplo 2: dois valores escalares 4 e 0 recebem pesos de atenção proporcionais a 3 e 1; após normalização, os pesos são 0,75 e 0,25 e a combinação é 3. O estudante deve calcular os pesos e explicar que eles não são, automaticamente, medidas de importância causal.

</div>

## Laboratório: aplicação e verificação

**Dados da aula:** [`dados.csv`](../../dados/aula/aula_01/dados.csv), [`rotulos.csv`](../../dados/aula/aula_01/rotulos.csv). **Todos são didáticos/sintéticos.**

### Problema de decisão e dados disponibilizados

**Situação.** Uma rede fictícia de cafeterias precisa compreender reclamações de clientes sem atribuir experiências a pessoas identificáveis. O produto é um painel de temas acompanhado de evidências literais, não um diagnóstico automático de intenção de compra.

**Pacote de dados.** `dados.csv`: 36 avaliações fictícias, três marcas, colunas `id`, `marca`, `nota` e `texto`. Incluir elogios mistos, negações, um comentário vazio e uma ironia. `rotulos.csv`: seis casos de referência examinados previamente pelo professor.

### Laboratório em aula (60 minutos)

1.  Conferir os 36 registros e comparar manualmente três comentários: elogio inequívoco, crítica e caso ambíguo.

2.  Especificar no Codex (interface gráfica) um painel com contagens por marca, temas propostos, frases de apoio e campo “evidência insuficiente”.

3.  Solicitar testes de existência de IDs, contagens e correspondência literal entre as citações e os textos de origem; inspecionar dois casos problemáticos.

4.  Interpretar em conjunto: diferença entre relato observado, tema sugerido e afirmação não sustentada.

### Especificação inicial por prompt

> **Crie um painel local em Python para ler os 36 comentários fictícios, organizar temas com exemplos literais e registrar afirmações incertas. Gere testes das contagens e das citações. Construa e execute tudo sem API convencional; quando necessário, integre o Codex Python SDK apenas após validar o ambiente.**

### Critérios de aceitação

Nenhuma citação inexistente; 36 IDs preservados; informação ausente nunca inventada; pelo menos um caso classificado como inconclusivo; registro de duas falhas efetivamente encontradas nos testes.

### Articulação com as demais aulas

A aula seguinte substitui a comparação impressionista de textos por uma representação vetorial mensurável. O arquivo de avaliações analisado aqui constitui a primeira versão do Projeto 1.

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

Não há quiz inicial neste encontro.

[Questões formativas de treinamento](../../apoio/treino.md#aula-01) (não são as questões da avaliação oficial).

## Referências para aprofundamento

Consulte a [bibliografia da disciplina](../../apoio/bibliografia.md) e as fontes técnicas indicadas no material específico.


## Simulação interativa

[Experimentar os parâmetros numéricos](../../assets/simuladores/index.html). A simulação complementa, mas não substitui, os cálculos feitos em papel.
