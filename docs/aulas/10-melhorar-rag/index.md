<div class="lesson-kicker">AULA 10 <span>·</span> MACROECONOMIA E FINANÇAS <span>·</span> 120 MINUTOS</div>

# Melhorar RAG sem perder rigor

<p class="lesson-lede">Quando aumentar o número de trechos recuperados melhora a resposta e quando apenas acrescenta ruído?</p>

<div class="case-strip"><span class="case-label">O problema</span>Perguntas sobre datas e mudanças de margem exigem dois documentos e cálculos, mas resultados irrelevantes disputam o contexto.</div>

!!! abstract "Resultados de aprendizagem"
    - **1.** Granularidade de chunks e sobreposição.
    - **2.** Retrieval híbrido e reranking.
    - **3.** Qualidade versus custo e latência.
    - **4.** Ablação e comparação justa.

<div class="lesson-actions"><a href="aula.ipynb" download>↓ Notebook guiado</a><a href="slides/aula.html" target="_blank">▣ Slides</a><a href="opcionais/">+ Ampliação</a></div>

<div class="lesson-mini">Conceitos · granularidade de chunks e sobreposição, retrieval híbrido e reranking, qualidade versus custo e latência, ablação e comparação justa</div>

---


## 1. Melhorar é comparar hipóteses

A etapa de avaliação identificou erros de recuperação e de geração. Agora vamos modificar uma variável por vez. Exemplos: quantidade de trechos \(k\), comprimento do chunk, sobreposição, forma de busca e existência de reranking. Uma comparação é informativa quando utiliza **as mesmas perguntas e os mesmos critérios**.

## 2. Um custo pouco visível

Recuperar dez trechos em lugar de três pode elevar a chance de incluir a fonte necessária, mas também acrescenta textos contraditórios ou irrelevantes, eleva o número de tokens e piora a capacidade do modelo de localizar o trecho decisivo. Não existe relação monotônica garantida entre \(k\) e correção da resposta final.

## 3. Busca híbrida

Um mecanismo lexical é forte em nomes, números e identificadores. Embeddings podem recuperar equivalências de significado. Busca híbrida combina os dois sinais, mas precisa de regras claras de pontuação e avaliação. **Reranking** reordena candidatos com um mecanismo mais caro e normalmente deve vir depois de uma recuperação inicial ampla.

!!! example "Duas falhas, duas intervenções"
    **Falha A:** o relatório 2026-T2 nunca aparece. Melhorar recuperação pode ajudar.  
    **Falha B:** o relatório aparece em primeiro lugar, mas o assistente confunde margem líquida com operacional. Alterar \(k\) pode não resolver; precisamos melhorar extração, cálculo ou instruções.

## 4. Uma tabela de experimentos

Registre para cada variante: Recall@k, respostas exatas, abstenções adequadas, custo estimado em tokens e erros por tipo. Faça os ajustes no conjunto de desenvolvimento; reserve perguntas novas para o teste final. Uma melhora de 6/8 para 7/8 é uma observação em poucos casos, não prova robusta de superioridade.

### Macroeconomia exige cronologia

O comunicado mais recente não é necessariamente a fonte correta para uma pergunta sobre o passado. Datas e períodos devem fazer parte dos metadados de recuperação. Uma fonte sem data pode ser semanticamente parecida, mas historicamente inadequada.


## Laboratório interativo

Antes de realizar a atividade, **registre um palpite**. Depois altere os parâmetros, observe a resposta e explique a divergência. O simulador executa operações locais: não inventa acesso a dados nem faz chamadas a um LLM real.

<div class="sim-shell"><iframe src="../../assets/simuladores/laboratorio.html?modulo=10" title="Laboratório interativo da aula 10" loading="lazy"></iframe></div>

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

1. Testar k=1,2,4 sobre perguntas com gabarito.
2. Variar lexical, híbrido e tamanho de chunk mantendo as perguntas fixas.
3. Identificar trade-offs e evitar ajuste sobre o teste final.

**Produto da aula:** Comparação controlada de três variantes de RAG com relatório de erros.

## Exercício para a semana

Entregue no Blackboard, individualmente, **um registro conciso** (até duas páginas ou notebook com comentários) que documente: (a) a pergunta e o método; (b) os dados utilizados, seus períodos e unidades; (c) dois resultados reproduzíveis; (d) pelo menos uma limitação; (e) uma verificação independente de uma conclusão produzida com IA. O arquivo será mantido para documentação, **sem nota própria**. Os conceitos serão avaliados no quiz seguinte.

## Para conferir a compreensão

**Pergunta central:** Aumentar k de 2 para 10 garante aumento da fidelidade da resposta final?

Responda sem utilizar o simulador. A solução comentada será retomada no quiz correspondente. Não memorize comandos: explique o conceito e o motivo da escolha.

---

<div class="lesson-footnav"><a href="../09-avaliacao-rag/">← Anterior</a><a href="../11-agentes-e-workflows/">Próximo →</a></div>
