<div class="lesson-kicker">AULA 01 <span>·</span> MARKETING <span>·</span> 120 MINUTOS</div>

# O que um LLM faz — e o que não faz

<p class="lesson-lede">Por que um LLM pode escrever uma previsão convincente de vendas sem possuir os dados necessários?</p>

<div class="case-strip"><span class="case-label">O problema</span>Uma rede varejista pergunta quanto venderá na próxima semana. O LLM responde com segurança, mas não conhece a série de vendas.</div>

!!! abstract "Resultados de aprendizagem"
    - **1.** Tokens e previsão do próximo token.
    - **2.** Distribuição de probabilidades e temperatura.
    - **3.** Contexto, atenção causal e limites do conhecimento.
    - **4.** Llm generativo versus modelo preditivo.

<div class="lesson-actions"><a href="aula.ipynb" download>↓ Notebook guiado</a><a href="slides/aula.html" target="_blank">▣ Slides</a><a href="opcionais/">+ Ampliação</a></div>

<div class="lesson-mini">Conceitos · tokens e previsão do próximo token, distribuição de probabilidades e temperatura, contexto, atenção causal e limites do conhecimento, LLM generativo versus modelo preditivo</div>

---


## 1. Uma pergunta que esconde duas tarefas

Uma empresa deseja estimar o faturamento da semana seguinte. Há duas questões distintas. A primeira é **predizer uma variável observável** usando uma base de dados, um critério de erro e uma avaliação fora da amostra. A segunda é **redigir uma resposta plausível** a uma pergunta em linguagem natural. Um modelo de linguagem pode desempenhar a segunda tarefa sem ter realizado a primeira.

A distinção é fundamental em Administração e Economia. Uma frase numérica não constitui, por si, uma estimativa. Para que haja previsão, precisamos identificar a variável-alvo, o instante em que a previsão será feita, as informações disponíveis naquele instante e uma forma de medir o erro.

!!! example "Estudo de caso: varejo"
    O gerente apresenta ao assistente apenas a frase: *"Preveja nosso faturamento da semana que vem"*. O sistema devolve R$ 320 mil e comenta que haverá crescimento de 8%. Sem a série histórica, calendário, localização ou sazonalidade, não há base verificável para os números. A resposta adequada é solicitar dados ou declarar explicitamente que se trata de uma hipótese ilustrativa.

## 2. A geração token a token

Um LLM transforma o texto de entrada em **tokens** e atribui uma distribuição de probabilidades ao próximo token. A resposta é produzida repetindo esse mecanismo, incorporando o token escolhido ao contexto. Esquematicamente,

\[
P(t_1,\ldots,t_m\mid c)=\prod_{j=1}^{m}P(t_j\mid c,t_1,\ldots,t_{j-1}).
\]

O condicionamento explica a utilidade de instruções e documentos adicionados ao prompt. Não assegura, porém, que uma proposição gerada seja verdadeira. Temperatura controla a dispersão da distribuição utilizada para selecionar tokens: valores altos tendem a admitir alternativas menos prováveis, sem fornecer conhecimento adicional.

Uma janela de contexto comporta um número finito de tokens. Incluir relatórios inteiros consome espaço e recursos; não equivale a criar uma base de dados confiável.

## 3. Atenção, contexto e um equívoco comum

No Transformer causal, o cálculo da atenção para um token considera os tokens anteriores e o próprio token, mas não os futuros. Não precisamos derivar as matrizes de atenção neste curso. Precisamos compreender a consequência operacional: o modelo escreve uma resposta em sequência e pode precisar de revisão, ferramentas ou informações externas para executar uma tarefa com precisão.

**Atenção não é citação.** Um modelo pode utilizar uma frase do contexto sem preservá-la literalmente e pode misturar elementos de fontes distintas. A verificação posterior permanece necessária.

## 4. Um protocolo de uso

Antes de aceitar qualquer resposta quantitativa, identifique a fonte, o período, a unidade, o método e a incerteza. Aplique a pergunta de controle: *"O que o sistema poderia saber com as informações que recebeu?"*. Uma resposta negativa é um diagnóstico, não um fracasso da tecnologia.

### Exemplo resolvido

Uma série de vendas semanais tem valores 100, 110, 90 e 120 (mil reais). Um baseline elementar para a próxima semana é a média, **R$ 105 mil**. Esse número é calculável, mas ainda não sabemos seu erro futuro. A resposta inventada de R$ 320 mil não tem sequer esse fundamento.


## Laboratório interativo

Antes de realizar a atividade, **registre um palpite**. Depois altere os parâmetros, observe a resposta e explique a divergência. O simulador executa operações locais: não inventa acesso a dados nem faz chamadas a um LLM real.

<div class="sim-shell"><iframe src="../../assets/simuladores/laboratorio.html?modulo=1" title="Laboratório interativo da aula 1" loading="lazy"></iframe></div>

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

1. Alterar temperatura e observar a concentração das probabilidades no simulador.
2. Comparar uma previsão produzida sem dados com um baseline calculado sobre uma série curta.
3. Escrever uma resposta que explicite ausência de evidência em vez de inventar números.

**Produto da aula:** Ficha experimental de três respostas ao mesmo pedido, com fontes e limites explícitos.

## Exercício para a semana

Entregue no Blackboard, individualmente, **um registro conciso** (até duas páginas ou notebook com comentários) que documente: (a) a pergunta e o método; (b) os dados utilizados, seus períodos e unidades; (c) dois resultados reproduzíveis; (d) pelo menos uma limitação; (e) uma verificação independente de uma conclusão produzida com IA. O arquivo será mantido para documentação, **sem nota própria**. Os conceitos serão avaliados no quiz seguinte.

## Para conferir a compreensão

**Pergunta central:** O LLM não recebeu vendas passadas; sua resposta de R$ 320 mil constitui uma previsão estatística validada?

Responda sem utilizar o simulador. A solução comentada será retomada no quiz correspondente. Não memorize comandos: explique o conceito e o motivo da escolha.

---

<div class="lesson-footnav"><a href="../../">← Anterior</a><a href="../02-embeddings-e-concorrencia/">Próximo →</a></div>
