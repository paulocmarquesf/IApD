# Integração de ferramentas computacionais

<span class="eyebrow">Aula 05 · Finanças</span>

> **Propósito:** Que operações um assistente deve delegar a ferramentas em vez de responder por aproximação linguística?

**Organização do encontro:** 15 minutos de quiz inicial (aulas 2 a 12); 45 minutos de conceitos e exercícios; 60 minutos de laboratório. A Aula 1 reserva 60 minutos para conceitos e 60 para o laboratório, sem quiz prévio.

**Objetivos:** Explicar o ciclo de tool calling, reconhecer esquemas e argumentos de ferramentas e avaliar cálculos financeiros obtidos por execução determinística.

## Fundamentação conceitual

### 1. Modelo de linguagem e ferramenta determinística

Um LLM pode escolher uma ferramenta e preparar seus argumentos, mas **não é a ferramenta**. O processo pode ser representado por quatro etapas: identificação da necessidade, preparação de parâmetros, execução verificável e comunicação do resultado. O rastro deve conter entrada, nome da função, argumentos, retorno e interpretação. Uma frase como «calculei a covariância» sem registro da chamada ou da operação não demonstra que ela foi executada.

Um *tool schema* especifica tipos e parâmetros. A validade da chamada é diferente da correção dos argumentos. Se o período solicitado é mensal, uma função que recebe preços diários requer uma decisão explícita sobre agregação, calendário e tratamento de dados faltantes.

### 2. Retorno e risco

Para preços ajustados $P_{t-1},P_t$, o retorno simples é

$$
r_t=\frac{P_t-P_{t-1}}{P_{t-1}}.
$$

Retornos simples se compõem multiplicativamente: $1+R=\prod_t(1+r_t)$. Assim, um aumento de 5% seguido de uma queda de 2% produz $(1{,}05)(0{,}98)-1=2{,}9\%$, e não 3%. Os dados de preços e os ajustes por proventos precisam ser definidos antes de calcular retornos.

Para dois ativos com pesos $w_A,w_B$ e covariância $\sigma_{AB}$, a variância da carteira é

$$
\sigma_p^2=w_A^2\sigma_A^2+w_B^2\sigma_B^2+2w_Aw_B\sigma_{AB},\quad
\sigma_{AB}=\rho_{AB}\sigma_A\sigma_B.
$$

Se $w_A=0{,}6$, $w_B=0{,}4$, $\sigma_A=20\%$, $\sigma_B=10\%$ e $\rho_{AB}=0{,}25$, a variância é $0{,}0184$ e a volatilidade é aproximadamente $13{,}565\%$. Não se deve substituir a variância da carteira pela média ponderada das volatilidades.

O índice de Sharpe, $S=(\mathbb E[R_p]-r_f)/\sigma_p$, exige que retorno, taxa livre de risco e volatilidade estejam na **mesma frequência temporal**.

### 3. Fronteira eficiente e limites de interpretação

O problema de Markowitz pode ser escrito como $\min_w w^\top\Sigma w$ sujeito a $\mathbf1^\top w=1$ e $\mu^\top w\ge r_0$, acrescido das restrições de investimento aplicáveis. O Codex pode gerar toda a rotina de preparação, otimização e visualização, mas o aluno deve verificar as premissas, a viabilidade das restrições e as unidades.

A atividade é metodológica, não uma recomendação de investimento. Dados sintéticos permitem confrontar os resultados com cálculos de referência e examinar sensibilidade à correlação.

## Exemplo de discussão para resolução manual

<div class="tcolorbox">

Duas ações têm retornos esperados de $10\%$ e $5\%$, volatilidades de $20\%$ e $10\%$, e correlação de $0{,}25$. Para pesos $0{,}6$ e $0{,}4$, obter $\mathbb E[r_p]=0{,}08$, $\operatorname{Var}(r_p)=0{,}0184$ e $\sigma_p\approx13{,}56\%$. Para taxa livre de risco de $2\%$, o índice de Sharpe é aproximadamente $0{,}442$. Identificar quais grandezas vêm dos dados e qual função calcula cada resultado.

</div>

## Laboratório: aplicação e verificação

**Dados da aula:** [`parametros.csv`](../../dados/aula/aula_05/parametros.csv), [`precos.csv`](../../dados/aula/aula_05/precos.csv). **Todos são didáticos/sintéticos.**

### Problema de decisão e dados disponibilizados

**Situação.** Um analista compara carteiras a partir de preços históricos. O LLM poderá explicar os resultados, mas cálculos e regras de risco devem ser executados por ferramentas determinísticas.

**Pacote de dados.** `precos.csv`: preços ajustados mensais sintéticos de três ativos ao longo de 24 meses; `parametros.csv`: taxa de referência e restrição de pesos não negativos com soma igual a 1. Valores explicitamente didáticos, sem recomendações de investimento.

### Laboratório em aula (60 minutos)

1.  Recalcular manualmente dois retornos e a variância de uma carteira com dois ativos.

2.  Solicitar ao Codex aplicativo com alinhamento de datas, retornos, covariância, fronteira ilustrativa e Sharpe com frequências compatíveis.

3.  Testar um portfólio 100% em um ativo, soma dos pesos, datas ausentes e covariância simétrica; confrontar dois resultados com contas manuais.

4.  Explorar carteira de maior retorno e de maior Sharpe, registrando limitações das estimativas.

### Especificação inicial por prompt

> **Construa um analisador local de carteiras com dados do CSV, sem API convencional. Faça todos os cálculos por Python, exiba fórmulas e unidades, teste datas faltantes e limites de pesos. Qualquer explicação textual por modelo deve citar resultados realmente calculados.**

### Critérios de aceitação

Pesos totalizam 1 dentro da tolerância; retornos e unidades consistentes; risco obtido de covariâncias; curvas identificam restrições; nenhuma conclusão é apresentada como aconselhamento financeiro.

### Articulação com as demais aulas

A Aula 6 trabalha não apenas uma ferramenta de cálculo, mas o encadeamento de fontes e operações para produzir uma análise de negócio.

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

O quiz oficial de 15 minutos no início da aula cobre os conceitos da Aula 4 e a atividade correspondente, condicionada ao depósito no GitHub. As questões oficiais e o gabarito são reservados ao professor.

[Questões formativas de treinamento](../../apoio/treino.md#aula-05) (não são as questões da avaliação oficial).

## Referências para aprofundamento

Consulte a [bibliografia da disciplina](../../apoio/bibliografia.md) e as fontes técnicas indicadas no material específico.
