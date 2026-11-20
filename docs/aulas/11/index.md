# Workflows e agentes de IA

<span class="eyebrow">Aula 11 · Operações empresariais</span>

> **Propósito:** Quem escolhe o próximo passo e como demonstrar que o processo termina no estado correto?

**Organização do encontro:** 15 minutos de quiz inicial (aulas 2 a 12); 45 minutos de conceitos e exercícios; 60 minutos de laboratório. A Aula 1 reserva 60 minutos para conceitos e 60 para o laboratório, sem quiz prévio.

**Objetivos:** Distinguir workflow predefinido de comportamento agentivo, modelar estados e transições e instrumentar chamadas de ferramentas em ambiente simulado.

## Fundamentação conceitual

### 1. Fluxos determinísticos e decisões delegadas

Um *workflow* especifica antecipadamente etapas, estados, condições e rotas possíveis. Um agente pode decidir dinamicamente qual ferramenta utilizar e quais passos seguir, dentro de permissões definidas. A distinção não é binária: uma aplicação pode ter partes determinísticas e trechos delegados ao modelo. Em todos os casos, efeitos sobre sistemas externos devem permanecer sujeitos a regras de autorização.

O estado $S_t$ pode incluir identificador do pedido, data de entrega, motivo da solicitação, status da aprovação e resultado de cada ferramenta. Uma transição é uma função $S_{t+1}=F(S_t,a_t,o_t)$, em que $a_t$ é ação proposta e $o_t$ é retorno observado. Os estados e transições precisam ser auditáveis.

### 2. Exemplo de política de devolução

Suponha uma política didática: devoluções por arrependimento podem ser solicitadas até 7 dias após recebimento; depois desse prazo, o sistema encaminha para análise humana. Para um pedido entregue há 5 dias, a condição temporal é satisfeita; entregue há 9 dias, não é. O prazo não deve ser inventado pelo LLM, mas consultado na política efetivamente fornecida. Situações de defeito podem exigir outra rota; o exemplo não pretende representar a legislação aplicável.

A ferramenta `consultar_pedido` retorna data e situação. A ferramenta `consultar_politica` retorna a regra. A aplicação pode propor `abrir_solicitacao`, mas não deve executar `efetuar_estorno` sem aprovação explícita e verificável.

### 3. Controle de ações e idempotência

Um teste importante verifica se a repetição de uma solicitação não executa duas vezes o mesmo efeito. Esse princípio é conhecido como **idempotência operacional**. Um identificador único de requisição e um registro de status permitem rejeitar operações duplicadas. Limitar o número de passos do agente, registrar timeouts e exigir condição de parada previne loops.

### 4. Rastros e testes

O laboratório produzirá rastros com estado inicial, ferramentas chamadas, argumentos, retornos, condição avaliada e estado final. Um bom teste inclui pedidos elegíveis, inelegíveis, dados ausentes, políticas conflitantes e solicitações repetidas. Um agente com resposta textual correta mas com uma operação não autorizada executada **falhou**. A avaliação deve distinguir trajetória, resultado e respeito às permissões.

## Exemplo de discussão para resolução manual

<div class="tcolorbox">

Uma política sintética permite devoluções até sete dias após a entrega. Pedido X foi entregue há seis dias e o item consta como elegível; Pedido Y foi entregue há dez dias. Desenhar transições desde "solicitação_recebida" até "elegibilidade_verificada", usando data de entrega e política. Em Y, a aplicação não deve inventar uma exceção; deve negar conforme regra ou escalar para análise humana, segundo o contrato operacional. Comparar grafo com ciclo indevido versus grafo com condição de parada.

</div>

## Laboratório: aplicação e verificação

**Dados da aula:** [`eventos.csv`](../../dados/aula/aula_11/eventos.csv), [`pedidos.csv`](../../dados/aula/aula_11/pedidos.csv), [`politicas.md`](../../dados/aula/aula_11/politicas.md). **Todos são didáticos/sintéticos.**

### Problema de decisão e dados disponibilizados

**Situação.** Uma varejista deseja processar trocas e devoluções com estados verificáveis. O modelo pode interpretar linguagem, mas a autorização para mudar estados deve ser definida por regras de negócio.

**Pacote de dados.** `pedidos.csv`: 15 pedidos fictícios, datas de entrega e situação; `politicas.md`: regras sintéticas de sete dias e exceções; `eventos.csv`: casos de ferramenta indisponível, pedido desconhecido e solicitação duplicada.

### Laboratório em aula (60 minutos)

1.  Desenhar à mão grafo de estados recebido, identificado, verificado, aguardando-aprovacao, concluido e escalado, com duas guardas.

2.  Pedir ao Codex simulador visual com ferramentas de leitura, transições determinísticas e log de estado anterior/ação/resposta/estado posterior.

3.  Executar cinco cenários: elegível, fora do prazo, pedido inexistente, indisponibilidade e chamada duplicada.

4.  Comparar workflow determinístico com seleção supervisionada de ferramentas de leitura; jamais liberar escrita por simples texto do LLM.

### Especificação inicial por prompt

> **Crie simulador local de trocas/devoluções com estados, guardas e log auditável. Todos os efeitos devem ser fictícios. Implemente interfaces gráficas de inspeção, testes de erro, interrupção e retomada; ações de escrita exigem validação por código independente de modelos.**

### Critérios de aceitação

Estado final deriva de eventos persistidos; nenhuma guarda ignorada; ações duplicadas tratadas idempotentemente; falhas geram estado de exceção; rastros podem ser reconstituídos por pedido.

### Articulação com as demais aulas

A Aula 12 acrescenta política de permissões, aprovação humana e avaliação sistemática da segurança das trajetórias.

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

O quiz oficial de 15 minutos no início da aula cobre os conceitos da Aula 10 e a atividade correspondente, condicionada ao depósito no GitHub. As questões oficiais e o gabarito são reservados ao professor.

[Questões formativas de treinamento](../../apoio/treino.md#aula-11) (não são as questões da avaliação oficial).

## Referências para aprofundamento

Consulte a [bibliografia da disciplina](../../apoio/bibliografia.md) e as fontes técnicas indicadas no material específico.
