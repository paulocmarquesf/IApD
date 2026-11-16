<div class="lesson-kicker">AULA 08 <span>·</span> FINANÇAS E MACROECONOMIA <span>·</span> 120 MINUTOS</div>

# Laboratório RAG: relatórios e política monetária

<p class="lesson-lede">O mesmo RAG consegue responder a perguntas numéricas e interpretar comunicados macroeconômicos?</p>

<div class="case-strip"><span class="case-label">O problema</span>Um assistente consulta relatórios corporativos fictícios e comunicados macroeconômicos ilustrativos, com perguntas sobre dados ausentes.</div>

!!! abstract "Resultados de aprendizagem"
    - **1.** Respostas com fontes e períodos.
    - **2.** Busca híbrida.
    - **3.** Abstenção, completude e limites.
    - **4.** Manipulação de informações potencialmente atuais.

<div class="lesson-actions"><a href="aula.ipynb" download>↓ Notebook guiado</a><a href="slides/aula.html" target="_blank">▣ Slides</a><a href="opcionais/">+ Ampliação</a></div>

<div class="lesson-mini">Conceitos · respostas com fontes e períodos, busca híbrida, abstenção, completude e limites, manipulação de informações potencialmente atuais</div>

---


## 1. Dois tipos de documento

Relatórios trimestrais contêm grandezas e convenções de período: receita, margem, caixa e resultados. Comunicados de política monetária utilizam conceitos como inflação, atividade e expectativas, muitas vezes em linguagem qualitativa. Um mesmo sistema de RAG pode consultar ambos, desde que preserve a distinção entre afirmação numérica e interpretação textual.

Nesta aula, **todos os relatórios e comunicados são fictícios**. Isso permite avaliar cada resposta contra um material fechado. No uso profissional, dados do Banco Central, IBGE e empresas devem ser obtidos de fontes oficiais e datados.

## 2. Uma pergunta, mais de uma evidência

Considere: *"Como mudou a margem operacional entre 2026-T1 e 2026-T2?"* O assistente precisa recuperar **dois** documentos e calcular duas razões: 145/920 e 165/1000. As margens são aproximadamente 15,76% e 16,50%; a diferença é de **0,74 ponto percentual**, não de 0,74% de variação relativa. É um caso em que RAG e ferramenta de cálculo se complementam.

## 3. Interpretar sem inventar uma posição oficial

Um comunicado fictício afirma que expectativas permaneceram elevadas. A afirmação permite descrever o texto, mas não concluir que o Banco Central brasileiro aumentou a Selic. **Texto simulado não é comunicação institucional.** O assistente deve identificar no resultado se a fonte é fictícia e evitar o salto de interpretação para fato.

## 4. Um pequeno contrato de resposta

Cada resposta da aplicação deve conter: `resposta`, `fontes`, `periodos`, `nivel_de_suporte` e `limites`. Se nenhum trecho sustentar a resposta, o campo de suporte deve registrar ausência de evidência. Uma citação correta não garante uma inferência correta; por isso, também verificaremos as operações e as conclusões.

!!! warning "Falhas distintas"
    Se o documento correto não apareceu, o problema é de **retrieval**. Se apareceu mas a resposta trocou milhão por bilhão, o problema é de **geração ou extração**. Se a fonte é inadequada para uma afirmação atual, o problema é de **proveniência**. As correções são diferentes.


## Laboratório interativo

Antes de realizar a atividade, **registre um palpite**. Depois altere os parâmetros, observe a resposta e explique a divergência. O simulador executa operações locais: não inventa acesso a dados nem faz chamadas a um LLM real.

<div class="sim-shell"><iframe src="../../assets/simuladores/laboratorio.html?modulo=8" title="Laboratório interativo da aula 8" loading="lazy"></iframe></div>

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

1. Montar um corpus com relatórios e comunicados rotulados como fictícios.
2. Comparar respostas a perguntas factuais e interpretativas.
3. Registrar cobertura e justificativa para as abstenções.

**Produto da aula:** Assistente documental que responde a oito perguntas de teste, inclusive duas sem resposta no corpus.

## Exercício para a semana

Entregue no Blackboard, individualmente, **um registro conciso** (até duas páginas ou notebook com comentários) que documente: (a) a pergunta e o método; (b) os dados utilizados, seus períodos e unidades; (c) dois resultados reproduzíveis; (d) pelo menos uma limitação; (e) uma verificação independente de uma conclusão produzida com IA. O arquivo será mantido para documentação, **sem nota própria**. Os conceitos serão avaliados no quiz seguinte.

## Para conferir a compreensão

**Pergunta central:** Um comunicado fictício menciona inflação sem informar taxa oficial. O assistente pode preencher o número a partir do contexto?

Responda sem utilizar o simulador. A solução comentada será retomada no quiz correspondente. Não memorize comandos: explique o conceito e o motivo da escolha.

---

<div class="lesson-footnav"><a href="../07-rag-documentos/">← Anterior</a><a href="../09-avaliacao-rag/">Próximo →</a></div>
