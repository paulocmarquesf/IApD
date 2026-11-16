<div class="lesson-kicker">AULA 06 <span>·</span> FINANÇAS E MACROECONOMIA <span>·</span> 120 MINUTOS</div>

# Aplicações compostas: carteiras e indicadores

<p class="lesson-lede">Como combinar um LLM, um conjunto de dados e funções de análise sem confundir interpretação com evidência?</p>

<div class="case-strip"><span class="case-label">O problema</span>Um estudante compara três fundos fictícios e deseja um relatório que distinga retorno passado, risco e projeção.</div>

!!! abstract "Resultados de aprendizagem"
    - **1.** Encadeamento de etapas.
    - **2.** Regressão e classificação instrumentais.
    - **3.** Retorno e volatilidade histórica.
    - **4.** Rastreabilidade de dados e resultados.

<div class="lesson-actions"><a href="aula.ipynb" download>↓ Notebook guiado</a><a href="slides/aula.html" target="_blank">▣ Slides</a><a href="opcionais/">+ Ampliação</a></div>

<div class="lesson-mini">Conceitos · encadeamento de etapas, regressão e classificação instrumentais, retorno e volatilidade histórica, rastreabilidade de dados e resultados</div>

---


## 1. Aplicações que combinam competências

Uma aplicação de IA para decisão nem sempre requer um agente autônomo. Um fluxo de etapas previsível é frequentemente preferível: ler o arquivo, validar colunas, calcular estatísticas e produzir um relatório. Um LLM pode explicar as etapas e auxiliar na programação, mas o cálculo deve permanecer inspecionável.

Usaremos três séries de cotas fictícias. O retorno simples entre dois instantes consecutivos é

\[
r_t=\frac{P_t}{P_{t-1}}-1.\]

É indispensável informar a frequência da série. Um retorno mensal não é um retorno anual. Uma volatilidade calculada em retornos mensais também é uma medida mensal, a menos que seja transformada com hipóteses apropriadas.

## 2. Uma distinção de interpretação

Em nossa atividade, `fundo_alpha`, `fundo_beta` e `renda_curta` são nomes de séries simuladas, não produtos reais. Podemos descrever médias, desvios e correlações, mas não deduzir qualidade de gestão, risco futuro ou recomendação personalizada. Resultados históricos dependem do intervalo escolhido.

!!! example "Exemplo numérico"
    Uma cota sobe de 100 para 103: retorno simples = **3%**. Se no mês seguinte ela cai de 103 para 100, o segundo retorno é aproximadamente **−2,91%**. A média aritmética dos dois retornos não substitui o retorno acumulado, que neste exemplo é zero.

## 3. Um painel de indicadores macroeconômicos

Além das cotas, temos série *inteiramente simulada* de inflação mensal, juros anuais, desemprego e expectativa para doze meses. A frequência e a unidade diferem entre colunas: somar a taxa mensal de inflação à taxa anual de juros não faz sentido. Mesmo um gráfico visualmente impecável pode sustentar uma comparação inválida.

No caso da inflação, a taxa acumulada de meses sucessivos é obtida pelo produto dos fatores \((1+\pi_t)\), não pela soma exata das taxas. Para dois meses de 1%, a inflação acumulada é 2,01%.

## 4. Comparar dois desenhos

**Pipeline fixo:** sempre roda as mesmas funções. É previsível e fácil de testar. **Assistente com ferramentas:** interpreta perguntas variadas e seleciona a função adequada. É flexível, mas acrescenta riscos de seleção incorreta, argumentos inadequados e explicações sem fundamento. No problema de hoje, o pipeline fixo resolve a maior parte da tarefa.

### Antes de decidir

Toda síntese deve trazer fonte dos dados, período, unidade e método. Em finanças e macroeconomia, esses quatro elementos fazem parte da própria afirmação, e não de uma nota de rodapé.


## Laboratório interativo

Antes de realizar a atividade, **registre um palpite**. Depois altere os parâmetros, observe a resposta e explique a divergência. O simulador executa operações locais: não inventa acesso a dados nem faz chamadas a um LLM real.

<div class="sim-shell"><iframe src="../../assets/simuladores/laboratorio.html?modulo=6" title="Laboratório interativo da aula 6" loading="lazy"></iframe></div>

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

1. Calcular retornos mensais de três cotas simuladas.
2. Comparar dispersão de retornos e média sem declarar qual fundo é melhor.
3. Separar, no relatório, contas reproduzíveis e interpretações do assistente.

**Produto da aula:** Miniaplicação que calcula retornos, volatilidades e produz síntese com fontes dos números.

## Exercício para a semana

Entregue no Blackboard, individualmente, **um registro conciso** (até duas páginas ou notebook com comentários) que documente: (a) a pergunta e o método; (b) os dados utilizados, seus períodos e unidades; (c) dois resultados reproduzíveis; (d) pelo menos uma limitação; (e) uma verificação independente de uma conclusão produzida com IA. O arquivo será mantido para documentação, **sem nota própria**. Os conceitos serão avaliados no quiz seguinte.

## Para conferir a compreensão

**Pergunta central:** Uma cota vai de 100 para 103 em um mês. Qual foi o retorno simples?

Responda sem utilizar o simulador. A solução comentada será retomada no quiz correspondente. Não memorize comandos: explique o conceito e o motivo da escolha.

---

<div class="lesson-footnav"><a href="../05-ferramentas-e-calculos/">← Anterior</a><a href="../07-rag-documentos/">Próximo →</a></div>
