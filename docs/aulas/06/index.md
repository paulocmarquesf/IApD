# Composição de aplicações com LLMs

<span class="eyebrow">Aula 06 · Marketing Analítico</span>

> **Propósito:** Como integrar informações de fontes distintas e preservar a origem de cada conclusão?

**Organização do encontro:** 15 minutos de quiz inicial (aulas 2 a 12); 45 minutos de conceitos e exercícios; 60 minutos de laboratório. A Aula 1 reserva 60 minutos para conceitos e 60 para o laboratório, sem quiz prévio.

**Objetivos:** Projetar fluxos compostos, identificar dependências entre ferramentas e distinguir informação observada, cálculo derivado e inferência do modelo.

## Fundamentação conceitual

### 1. Aplicações como composição de operações

Uma aplicação composta transforma a saída de uma operação em entrada de outra. Se $f$ prepara avaliações, $g$ recupera textos semelhantes e $h$ combina indicadores comerciais, o resultado é $h(g(f(x)),z)$, em que $z$ reúne preços e participações provenientes de uma base **independente**. A composição precisa respeitar dependências, tipos, unidades e proveniência; uma operação isolada correta não garante que o sistema completo esteja correto.

Um grafo acíclico de tarefas torna explícitas as relações entre etapas. Para cada aresta, o aluno deve perguntar: «Qual dado passou? Que transformação foi aplicada? Que informação foi perdida?». Campos com mesma aparência mas sem mesmo significado não podem ser combinados automaticamente.

### 2. Proveniência e temporalidade

Um relatório sobre posicionamento pode reunir avaliações coletadas em determinado mês, preços vigentes em outra data e participação de mercado aferida em um período anual. Somar essas informações sem registrar suas datas cria uma aparência de precisão que não existe. Toda saída deve identificar de onde veio cada número, qual transformação o produziu e quais premissas são necessárias para interpretá-lo.

Considere preços de R\$ 120 e R\$ 150. A diferença relativa a 150 é $30/150=20\%$; relativa a 120 é $30/120=25\%$. Um assistente que afirma «a marca A é 25% mais barata que B» escolheu a base errada se pretende medir desconto em relação a B. A noção de porcentagem exige denominador explícito.

### 3. Falhas de integração

Quatro erros merecem especial atenção: (i) ferramenta não executada; (ii) argumento incorreto ou de unidade incompatível; (iii) retorno correto atribuído à entidade errada; (iv) inferência não sustentada apresentada como fato. Um rastro de execução útil permite localizar essas falhas.

A participação de mercado **não** pode ser estimada somente a partir da proporção de avaliações de determinada marca: o número de reviews depende de cobertura, propensão a avaliar e exposição. Comparar a percepção textual com participação já observada é legítimo; deduzir participação diretamente do volume de reviews, sem desenho amostral apropriado, não é.

### 4. Verificação de ponta a ponta

O laboratório deve produzir uma tabela final acompanhada de um registro de origens. Testes unitários verificam cada ferramenta; testes de integração verificam a correspondência correta entre marca, data e indicador. O aluno deverá fornecer pelo menos um exemplo em que cada componente funciona isoladamente, mas a associação final é incorreta.

## Exemplo de discussão para resolução manual

<div class="tcolorbox">

Uma ferramenta retorna preços A=R\$ 100 e B=R\$ 120 no mesmo período; outra retorna que 30 de 50 avaliações de A mencionam durabilidade. Calcular diferença percentual de preços em relação a A: $(120-100)/100=20\%$; frequência de menções em A: 30/50=60%. Perguntar se podemos concluir que A tem 60% de participação no mercado (não) ou que B é 20% mais caro em todo o mercado (apenas nesta observação). Desenhar o grafo de dependências dessas duas conclusões.

</div>

## Laboratório: aplicação e verificação

**Dados da aula:** [`avaliacoes.csv`](../../dados/aula/aula_06/avaliacoes.csv), [`pesquisa.csv`](../../dados/aula/aula_06/pesquisa.csv), [`precos.csv`](../../dados/aula/aula_06/precos.csv). **Todos são didáticos/sintéticos.**

### Problema de decisão e dados disponibilizados

**Situação.** Uma empresa deseja comparar posicionamento e preço de concorrentes. A análise deve distinguir avaliações, preços e participação de mercado, cada qual com unidade, fonte e data próprias.

**Pacote de dados.** Pacote de referência de 48 avaliações e embeddings verificados; `precos.csv` com quatro marcas, data e unidade; `pesquisa.csv` com participação de mercado ilustrativa explicitamente observada em levantamento independente.

### Laboratório em aula (60 minutos)

1.  Mapear em papel quais conclusões cada fonte permite e quais não permite.

2.  Pedir ao Codex painel que una atributos mencionados, preços datados e participações somente quando o levantamento fornecer o denominador.

3.  Forçar um caso de dados conflitantes por data, unidade ou marca e verificar se o painel bloqueia comparação indevida.

4.  Redigir parecer curto com três afirmações rastreáveis e duas hipóteses não testadas.

### Especificação inicial por prompt

> **Amplie o painel de Marketing para combinar embeddings de avaliações com preços e dados explícitos de pesquisa de mercado. Exiba origem, data, denominadores e unidade de cada indicador; impeça inferir market share apenas de avaliações.**

### Critérios de aceitação

Toda afirmação numérica tem fonte; comparações usam datas/unidades compatíveis; participação de mercado nunca é inferida de frequência de comentários; conflito gera alerta visível.

### Articulação com as demais aulas

Encerramento do primeiro bloco e preparação para PI. A Aula 7 retoma o problema de fundamentação, agora em documentos longos e recuperados por busca.

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

O quiz oficial de 15 minutos no início da aula cobre os conceitos da Aula 5 e a atividade correspondente, condicionada ao depósito no GitHub. As questões oficiais e o gabarito são reservados ao professor.

[Questões formativas de treinamento](../../apoio/treino.md#aula-06) (não são as questões da avaliação oficial).

## Referências para aprofundamento

Consulte a [bibliografia da disciplina](../../apoio/bibliografia.md) e as fontes técnicas indicadas no material específico.
