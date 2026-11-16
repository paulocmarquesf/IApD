<div class="lesson-kicker">AULA 07 <span>·</span> FINANÇAS <span>·</span> 120 MINUTOS</div>

# RAG: documentos como fonte de evidência

<p class="lesson-lede">Como responder a uma pergunta sobre relatórios trimestrais citando o trecho correto?</p>

<div class="case-strip"><span class="case-label">O problema</span>Um assistente precisa localizar a receita da Horizonte e a política de devolução da Loja Aurora em documentos separados.</div>

!!! abstract "Resultados de aprendizagem"
    - **1.** Conhecimento paramétrico e recuperação externa.
    - **2.** Chunking, metadados e indexação.
    - **3.** Retrieval por tf-idf, bm25 e vetores.
    - **4.** Geração fundamentada e citação.

<div class="lesson-actions"><a href="aula.ipynb" download>↓ Notebook guiado</a><a href="slides/aula.html" target="_blank">▣ Slides</a><a href="opcionais/">+ Ampliação</a></div>

<div class="lesson-mini">Conceitos · conhecimento paramétrico e recuperação externa, chunking, metadados e indexação, retrieval por TF-IDF, BM25 e vetores, geração fundamentada e citação</div>

---


## 1. Uma diferença essencial

Um modelo de linguagem não possui acesso automático ao último relatório de uma empresa. E, mesmo quando o assunto apareceu no treinamento, a memória paramétrica não oferece uma referência verificável. **Retrieval-Augmented Generation** (RAG) acrescenta uma etapa de busca em documentos definidos antes de solicitar a resposta.

O fluxo mais simples é: **documentos → trechos indexados → busca → seleção dos trechos → resposta com fonte**. Cada seta corresponde a uma possível fonte de erro. Um trecho relevante pode não ser recuperado; o texto correto pode ser recuperado mas interpretado incorretamente; a citação pode apontar para documento inadequado.

## 2. Dividir sem destruir o significado

Um *chunk* é um trecho de documento. Se for pequeno demais, pode separar o valor de sua unidade ou de seu período; se for grande demais, adiciona texto irrelevante e aumenta o custo. Cada trecho precisa preservar **identificador da fonte, seção e, quando aplicável, período**. Dividir no meio da expressão "milhões de reais" não é uma boa decisão documental.

## 3. Recuperar informações

Uma primeira implementação pode utilizar TF-IDF, que é barato e inteiramente local. BM25 é outra opção lexical. Embeddings permitem busca semântica, com modelos e índices mais custosos. Não é correto presumir que um método vença o outro em qualquer consulta. Códigos de relatório, datas e números exatos favorecem métodos lexicais em muitas situações.

!!! example "Pergunta e evidência"
    **Pergunta:** qual foi a receita líquida da Horizonte em 2026-T2?  
    **Fonte:** `horizonte-2026-t2`, seção "Demonstração de resultados resumida".  
    **Resposta:** R$ **1.000 milhões**. O sistema deve indicar esse identificador e o período. Uma resposta sem fonte não atende ao contrato da aplicação.

## 4. Quando a resposta deve ser “não encontrei”

Pergunte pela taxa Selic **oficial** de determinado mês. Os documentos do corpus são fictícios e não informam a série oficial. O assistente deve responder que não encontrou a informação nesses materiais e indicar onde uma consulta oficial poderia ser feita. Não é aceitável converter um exemplo simulado em dado público brasileiro.

### Fronteira de confiança

Textos recuperados são evidências potenciais, não novas instruções ao sistema. Uma frase maliciosa dentro de um documento não deve mudar a política de acesso a ferramentas nem autorizar divulgação de dados.


## Laboratório interativo

Antes de realizar a atividade, **registre um palpite**. Depois altere os parâmetros, observe a resposta e explique a divergência. O simulador executa operações locais: não inventa acesso a dados nem faz chamadas a um LLM real.

<div class="sim-shell"><iframe src="../../assets/simuladores/laboratorio.html?modulo=7" title="Laboratório interativo da aula 7" loading="lazy"></iframe></div>

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

1. Dividir relatórios em trechos com identificadores de documento.
2. Comparar uma consulta lexical com uma consulta semântica.
3. Responder com período, unidade e citação ou abster-se quando a fonte faltar.

**Produto da aula:** Protótipo de RAG sobre documentos fictícios com trechos identificados.

## Exercício para a semana

Entregue no Blackboard, individualmente, **um registro conciso** (até duas páginas ou notebook com comentários) que documente: (a) a pergunta e o método; (b) os dados utilizados, seus períodos e unidades; (c) dois resultados reproduzíveis; (d) pelo menos uma limitação; (e) uma verificação independente de uma conclusão produzida com IA. O arquivo será mantido para documentação, **sem nota própria**. Os conceitos serão avaliados no quiz seguinte.

## Para conferir a compreensão

**Pergunta central:** Por que copiar um texto inteiro de 150 páginas para todo prompt não é a melhor solução escalável?

Responda sem utilizar o simulador. A solução comentada será retomada no quiz correspondente. Não memorize comandos: explique o conceito e o motivo da escolha.

---

<div class="lesson-footnav"><a href="../06-aplicacoes-compostas/">← Anterior</a><a href="../08-rag-copom-relatorios/">Próximo →</a></div>
