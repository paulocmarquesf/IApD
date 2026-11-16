<div class="lesson-kicker">AULA 02 <span>·</span> MARKETING <span>·</span> 120 MINUTOS</div>

# Embeddings, similaridade e concorrência

<p class="lesson-lede">Como identificar produtos concorrentes quando as descrições usam palavras diferentes?</p>

<div class="case-strip"><span class="case-label">O problema</span>Uma loja compara dezesseis produtos por descrições; a busca por palavras perde sinônimos e a busca semântica aproxima usos semelhantes.</div>

!!! abstract "Resultados de aprendizagem"
    - **1.** Representações vetoriais.
    - **2.** Similaridade cosseno.
    - **3.** Busca lexical versus busca semântica.
    - **4.** Redução de dimensionalidade e agrupamento.

<div class="lesson-actions"><a href="aula.ipynb" download>↓ Notebook guiado</a><a href="slides/aula.html" target="_blank">▣ Slides</a><a href="opcionais/">+ Ampliação</a></div>

<div class="lesson-mini">Conceitos · representações vetoriais, similaridade cosseno, busca lexical versus busca semântica, redução de dimensionalidade e agrupamento</div>

---


## 1. Similaridade como problema de mercado

A proximidade de duas marcas não é uma propriedade absoluta. Ela depende dos atributos considerados e da forma como os consumidores avaliam substituição. Uma caneta e um caderno podem aparecer juntos em compras, mas não são necessariamente substitutos. Dois modelos de mochila podem ser substitutos sem partilhar muitas palavras na descrição.

No estudo da concorrência, a tarefa é representar cada produto por informações comparáveis. Uma estratégia clássica utiliza atributos observados e uma medida de dissimilaridade. Outra transforma descrições textuais em **embeddings**, vetores cuja geometria procura conservar aspectos do significado.

## 2. Vetores e cosseno

Se \(u,v\in\mathbb R^d\) são vetores não nulos, a similaridade cosseno é

\[
\operatorname{sim}(u,v)=\frac{u^\top v}{\lVert u\rVert\,\lVert v\rVert}.
\]

Vetores na mesma direção têm similaridade 1, independentemente de seus comprimentos; vetores ortogonais têm similaridade 0. A distância euclidiana pode mudar quando multiplicamos um vetor por uma constante, mesmo que o cosseno permaneça 1. Isso torna a escolha da métrica uma decisão substantiva.

!!! example "Uma conta curta"
    Para \(u=(3,0)\) e \(v=(6,0)\), o cosseno é 1 e a distância euclidiana é 3. Para \(u=(3,0)\) e \(w=(0,3)\), o cosseno é 0. O resultado não depende de escrevermos os componentes como características comerciais, mas a interpretação depende do que eles representam.

## 3. Palavras ou significado?

**Busca lexical**, como TF-IDF, valoriza a presença das palavras da consulta. **Busca semântica** usa embeddings para tentar encontrar expressões de sentido próximo. Uma pergunta sobre *"levar o computador na viagem"* pode encontrar uma mochila para notebook, mesmo sem a palavra *mochila* na consulta. Em contrapartida, o código exato de um SKU pode ser localizado com maior segurança por busca lexical.

A comparação justa exige um pequeno conjunto de perguntas e respostas de referência. Devemos separar o julgamento sobre a relevância do resultado da impressão de que a resposta *parece* convincente.

## 4. Visualizar sem simplificar demais

Projeções bidimensionais por PCA ou MDS facilitam a inspeção de relações, mas distorcem parte da geometria original. A distância no gráfico é aproximação, não comprovação de concorrência. Clustering produz uma partição segundo uma regra matemática; não descobre automaticamente segmentos economicamente válidos.

### Decisão empresarial

Um sistema de recomendações precisa escolher entre **substitutos** e **complementos**. Recomendação de complemento busca venda conjunta; análise de concorrência exige semelhança de função e preferência. O mesmo embedding pode apoiar ambas, mas a decisão final requer outra informação.


## Laboratório interativo

Antes de realizar a atividade, **registre um palpite**. Depois altere os parâmetros, observe a resposta e explique a divergência. O simulador executa operações locais: não inventa acesso a dados nem faz chamadas a um LLM real.

<div class="sim-shell"><iframe src="../../assets/simuladores/laboratorio.html?modulo=2" title="Laboratório interativo da aula 2" loading="lazy"></iframe></div>

## Roteiro da aula (120 minutos)

| Tempo | Trabalho | Evidência observável |
|---|---|---|
| 00–10 min | Apresentar o caso e formular a pergunta | Critério de sucesso escrito |
| 10–35 min | Conceitos centrais com exemplos | Palpites e cálculos conferidos |
| 35–50 min | Exploração do simulador | Uma observação e sua explicação |
| 50–80 min | Notebook guiado: executar, modificar, comparar | Saída reproduzível |
| 80–105 min | Exercício individual de aplicação | Resultado + diagnóstico de um limite |
| 105–120 min | Debate dos erros e síntese | Registro do que foi ou não demonstrado |

## Atividade individual

1. Mover vetores e calcular o cosseno de ângulos conhecidos.
2. Comparar descrições do catálogo com TF-IDF e embeddings opcionais.
3. Discutir quando produtos semanticamente semelhantes não são substitutos econômicos.

**Produto da aula:** Mapa comparativo de produtos e teste de três consultas lexicais e semânticas.

## Exercício para a semana

Entregue no Blackboard, individualmente, **um registro conciso** (até duas páginas ou notebook com comentários) que documente: (a) a pergunta e o método; (b) os dados utilizados, seus períodos e unidades; (c) dois resultados reproduzíveis; (d) pelo menos uma limitação; (e) uma verificação independente de uma conclusão produzida com IA. O arquivo será mantido para documentação, **sem nota própria**. Os conceitos serão avaliados no quiz seguinte.

## Para conferir a compreensão

**Pergunta central:** Dois vetores têm mesma direção e comprimentos distintos; qual é sua similaridade cosseno?

Responda sem utilizar o simulador. A solução comentada será retomada no quiz correspondente. Não memorize comandos: explique o conceito e o motivo da escolha.

---

<div class="lesson-footnav"><a href="../01-llms-e-limites/">← Anterior</a><a href="../03-saidas-estruturadas/">Próximo →</a></div>
