# Retrieval-Augmented Generation

<span class="eyebrow">Aula 07 · Macroeconomia</span>

> **Propósito:** Como uma aplicação identifica os trechos documentais que sustentam uma resposta?

**Organização do encontro:** 15 minutos de quiz inicial (aulas 2 a 12); 45 minutos de conceitos e exercícios; 60 minutos de laboratório. A Aula 1 reserva 60 minutos para conceitos e 60 para o laboratório, sem quiz prévio.

**Objetivos:** Compreender a arquitetura de RAG e separar erros de ingestão, recuperação e geração, com controle explícito de fontes e datas.

## Fundamentação conceitual

### 1. Recuperação antes da geração

Em *Retrieval-Augmented Generation* (RAG), a resposta é condicionada a trechos recuperados de um acervo. O mecanismo separa preparação do corpus, indexação, recuperação e geração. Essa distinção importa porque uma resposta pode ser incorreta por duas razões: a evidência não foi recuperada ou foi recuperada, mas o gerador não a utilizou adequadamente.

A preparação define documentos, metadados, política de fragmentação (*chunking*) e possíveis sobreposições. Fragmentos curtos podem perder o referente de expressões como «essa decisão»; longos demais podem reduzir precisão e ocupar desnecessariamente o contexto. A qualidade não depende de maximizar indiscriminadamente o número de trechos.

### 2. Recuperação e top-k

Se um índice retorna trechos $d_1,\ldots,d_m$ ordenados por relevância, *top-k* conserva apenas os $k$ primeiros. Considere a ordem $A,B,C,D$ e suponha que apenas $C$ contém a evidência. Com $k=2$, o gerador não recebe o trecho correto. Mesmo que escreva uma resposta plausível, ela não estará fundamentada pelo corpus fornecido.

A recuperação pode ser lexical (termos coincidentes), densa (vetores de embeddings) ou híbrida. A melhor abordagem depende da estrutura dos documentos e das perguntas. Nomes, datas e números exatos são frequentemente úteis para busca lexical; paráfrases podem favorecer busca densa.

### 3. Citações e distinção entre texto e interpretação

Uma citação documental exige identificador, data ou versão e localização do trecho. Uma resposta sobre determinada reunião do Copom não pode ser sustentada apenas por trecho verdadeiro, porém extraído de reunião diferente. É necessário preservar a dimensão temporal.

O sistema deve separar claramente (a) o que o documento afirma, (b) a síntese produzida pela aplicação e (c) interpretações adicionais do analista. Quando o acervo não responde à questão, a abstenção é um resultado legítimo. A saída não deve inventar falas nem atribuir ao Banco Central interpretações não presentes no documento.

### 4. Segurança documental e avaliação

Um texto recuperado pode conter instruções para o modelo. Essas instruções não têm a autoridade do prompt da aplicação. Deve-se tratar documentos como **dados não confiáveis** e testar tentativas de *prompt injection*. Para avaliar o retriever, criar perguntas com trechos relevantes identificados; para avaliar o gerador, conferir cada afirmação com a fonte correta.

No laboratório serão usados documentos didáticos explicitamente fictícios, com registros de reunião e data. Uma extensão opcional substitui esse conjunto por atas oficiais do Banco Central, com proveniência e versões congeladas para reprodução.

## Exemplo de discussão para resolução manual

<div class="tcolorbox">

Uma busca retorna quatro trechos com escores 0,87; 0,78; 0,61; 0,43. Com k=2, somente os dois primeiros entram no contexto da resposta. Se o trecho correto está na terceira posição, a recuperação falhou para k=2, mesmo que o modelo redija uma justificativa plausível. Compare um chunk muito curto, que perde o antecedente de "essa decisão", com outro longo, que inclui o parágrafo anterior. O estudante identifica o ponto de falha sem depender de software.

</div>

## Laboratório: aplicação e verificação

**Dados da aula:** [`documento_didatico_1.md`](../../dados/aula/aula_07/documento_didatico_1.md), [`documento_didatico_2.md`](../../dados/aula/aula_07/documento_didatico_2.md), [`documento_didatico_3.md`](../../dados/aula/aula_07/documento_didatico_3.md), [`perguntas.csv`](../../dados/aula/aula_07/perguntas.csv). **Todos são didáticos/sintéticos.**

### Problema de decisão e dados disponibilizados

**Situação.** Um pesquisador precisa identificar os argumentos apresentados pelo Copom em reuniões distintas e recuperar trechos verificáveis, sem atribuir ao comitê interpretações produzidas pelo sistema.

**Pacote de dados.** Pacote didático de três documentos fictícios de reuniões monetárias, com `data`, `reuniao`, `url` e texto; `perguntas.csv` com 12 consultas e trechos relevantes identificados. Uma extensão opcional poderá utilizar atas oficiais do Banco Central, com proveniência e versões verificadas.

### Laboratório em aula (60 minutos)

1.  Escolher manualmente a evidência para duas perguntas e registrar reunião/data em cada citação.

2.  Solicitar ao Codex extração, fragmentação, indexação local, recuperação top-k e resposta com citações por trecho.

3.  Alterar k e tamanho dos fragmentos; observar uma pergunta cuja resposta desaparece do contexto e outra envolvendo reuniões diferentes.

4.  Testar abstenção, referência temporal e tentativa de prompt injection dentro de trecho recuperado.

### Especificação inicial por prompt

> **Construa um RAG local sobre os três documentos didáticos. Mostre por pergunta os trechos recuperados, reunião, data, localização e resposta fundamentada. Permita abstenção; se houver geração por LLM, use apenas o Codex Python SDK previamente validado; mantenha modo de inspeção de recuperação sem geração.**

### Critérios de aceitação

Todas as citações apontam para trecho presente na ata correta; respostas sem evidência sinalizam insuficiência; versão de corpus e parâmetros de busca registrados; nenhuma inferência é apresentada como declaração literal do Banco Central.

### Articulação com as demais aulas

A Aula 8 reutilizará a lógica de recuperação em um sistema no qual as perguntas dependem do histórico da conversa.

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

O quiz oficial de 15 minutos no início da aula cobre os conceitos da Aula 6 e a atividade correspondente, condicionada ao depósito no GitHub. As questões oficiais e o gabarito são reservados ao professor.

[Questões formativas de treinamento](../../apoio/treino.md#aula-07) (não são as questões da avaliação oficial).

## Referências para aprofundamento

Consulte a [bibliografia da disciplina](../../apoio/bibliografia.md) e as fontes técnicas indicadas no material específico.


## Simulação interativa

[Experimentar os parâmetros numéricos](../../assets/simuladores/index.html). A simulação complementa, mas não substitui, os cálculos feitos em papel.
