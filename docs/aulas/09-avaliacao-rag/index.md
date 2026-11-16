<div class="lesson-kicker">AULA 09 <span>·</span> MARKETING E FINANÇAS <span>·</span> 120 MINUTOS</div>

# Avaliar RAG: recuperar e responder

<p class="lesson-lede">Como distinguir uma busca fraca de uma resposta mal fundamentada?</p>

<div class="case-strip"><span class="case-label">O problema</span>O assistente documental erra perguntas sobre receita, prazos de devolução e indicadores oficiais ausentes.</div>

!!! abstract "Resultados de aprendizagem"
    - **1.** Golden set e avaliação fora do desenvolvimento.
    - **2.** Recall@k e mrr.
    - **3.** Factualidade, suporte e citação.
    - **4.** Taxa de abstenção e erros por categoria.

<div class="lesson-actions"><a href="aula.ipynb" download>↓ Notebook guiado</a><a href="slides/aula.html" target="_blank">▣ Slides</a><a href="opcionais/">+ Ampliação</a></div>

<div class="lesson-mini">Conceitos · golden set e avaliação fora do desenvolvimento, Recall@k e MRR, factualidade, suporte e citação, taxa de abstenção e erros por categoria</div>

---


## 1. Um RAG tem dois componentes avaliáveis

A recuperação seleciona evidências; a geração interpreta essas evidências. Uma avaliação agregada de satisfação pode esconder a origem do erro. Precisamos de perguntas com documentos relevantes conhecidos e, separadamente, de respostas de referência ou critérios de julgamento.

Seja \(S_q\) o conjunto de fontes relevantes para uma pergunta \(q\) e \(R_q(k)\) o conjunto das primeiras \(k\) fontes recuperadas. Em casos com uma fonte relevante por pergunta, **Recall@k** é a fração de perguntas para as quais ela apareceu entre as primeiras \(k\). Com várias fontes, define-se por cobertura dos itens relevantes e explicita-se a forma de agregação.

## 2. Ordem importa

Duas buscas podem ter mesmo Recall@3 e utilidade diferente quando a fonte aparece na primeira posição ou na terceira. O *Mean Reciprocal Rank* (MRR) utiliza o inverso da posição da primeira fonte relevante. Não mede se o texto final está correto; mede o ordenamento.

!!! example "Exemplo resolvido"
    Em quatro perguntas, a primeira fonte relevante aparece nas posições 1, 2, 4 e não aparece. Considerando contribuição zero no último caso, o MRR é \((1+1/2+1/4+0)/4=0{,}4375\).

## 3. Avaliar o conteúdo

Uma resposta pode citar o documento certo e trocar o valor de receita. Portanto, devemos testar **exatidão numérica**, **suporte documental** e **citações** separadamente. Também distinguimos três comportamentos: resposta correta, resposta incorreta e abstenção adequada. Quando não existe fonte para a pergunta, responder “não encontrei” é um sucesso, não um erro.

## 4. Avaliação humana e automática

Juízes baseados em LLMs ajudam na escala, mas podem cometer erros e compartilhar vieses com o sistema avaliado. Recomendamos rubricas claras e revisão manual de uma amostra dos julgamentos. O laboratório utiliza uma base de oito perguntas: é pequena para fins científicos, mas suficiente para aprender a estrutura de uma avaliação.

### Diagnóstico

Ao apresentar uma métrica, informe sempre o conjunto de perguntas, seu tamanho, a versão da indexação e se as decisões de ajuste foram tomadas antes ou depois de observar o conjunto de teste.


## Laboratório interativo

Antes de realizar a atividade, **registre um palpite**. Depois altere os parâmetros, observe a resposta e explique a divergência. O simulador executa operações locais: não inventa acesso a dados nem faz chamadas a um LLM real.

<div class="sim-shell"><iframe src="../../assets/simuladores/laboratorio.html?modulo=9" title="Laboratório interativo da aula 9" loading="lazy"></iframe></div>

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

1. Calcular Recall@2 em ranking de documentos com referência.
2. Conferir manualmente duas respostas com citações.
3. Comparar um sistema que responde sempre com outro que se abstém quando necessário.

**Produto da aula:** Relatório de avaliação com tabela pergunta-fonte-evidência-resposta.

## Exercício para a semana

Entregue no Blackboard, individualmente, **um registro conciso** (até duas páginas ou notebook com comentários) que documente: (a) a pergunta e o método; (b) os dados utilizados, seus períodos e unidades; (c) dois resultados reproduzíveis; (d) pelo menos uma limitação; (e) uma verificação independente de uma conclusão produzida com IA. O arquivo será mantido para documentação, **sem nota própria**. Os conceitos serão avaliados no quiz seguinte.

## Para conferir a compreensão

**Pergunta central:** Em dez perguntas cuja fonte é conhecida, a busca coloca a fonte entre os dois primeiros em oito. Qual o Recall@2?

Responda sem utilizar o simulador. A solução comentada será retomada no quiz correspondente. Não memorize comandos: explique o conceito e o motivo da escolha.

---

<div class="lesson-footnav"><a href="../08-rag-copom-relatorios/">← Anterior</a><a href="../10-melhorar-rag/">Próximo →</a></div>
