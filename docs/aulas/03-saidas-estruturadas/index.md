<div class="lesson-kicker">AULA 03 <span>·</span> FINANÇAS <span>·</span> 120 MINUTOS</div>

# LLMs como componentes: extração estruturada

<p class="lesson-lede">Como transformar um trecho de relatório trimestral em dados que um programa possa verificar?</p>

<div class="case-strip"><span class="case-label">O problema</span>A empresa fictícia Horizonte publica receita, custos e lucro em um relatório resumido; o assistente deve retornar campos, unidades e fontes.</div>

!!! abstract "Resultados de aprendizagem"
    - **1.** Prompts claros e restrições.
    - **2.** Json e esquemas tipados.
    - **3.** Extração versus inferência.
    - **4.** Validade sintática versus verdade factual.

<div class="lesson-actions"><a href="aula.ipynb" download>↓ Notebook guiado</a><a href="slides/aula.html" target="_blank">▣ Slides</a><a href="opcionais/">+ Ampliação</a></div>

<div class="lesson-mini">Conceitos · prompts claros e restrições, JSON e esquemas tipados, extração versus inferência, validade sintática versus verdade factual</div>

---


## 1. Do texto ao dado

Uma análise de relatórios financeiros frequentemente começa por localizar grandezas simples: receita líquida, resultado operacional, lucro líquido, fluxo de caixa e período de referência. O interesse desta aula não é ensinar contabilidade avançada, mas mostrar como um LLM pode auxiliar na leitura sem se transformar em autoridade sobre os números.

A tarefa de extração exige um **contrato de saída**. Por exemplo: `empresa` é texto; `periodo` é texto; `receita_milhoes` é número ou nulo; `fonte` é texto. O formato facilita a automação, mas não substitui o exame do documento original.

## 2. Um esquema explícito

```json
{
  "empresa": "Horizonte Comércio S.A.",
  "periodo": "2026-T2",
  "receita_milhoes": 1000,
  "lucro_liquido_milhoes": 107,
  "fonte": "horizonte-2026-t2"
}
```

A palavra *milhões* é parte do campo, não uma ornamentação. Confundir R$ 1.000 milhões com R$ 1.000 cria um erro de três ordens de grandeza. **Saldo** de caixa em uma data e **fluxo** de caixa em um trimestre são conceitos distintos, embora ambos possam aparecer no mesmo relatório.

## 3. Validação não é verificação

Validar consiste em conferir se os campos existem e têm tipos compatíveis, se números estão em faixas aceitáveis e se o período foi informado. Verificar é confrontar cada valor com o documento. Uma resposta pode ser um JSON impecável e ainda apresentar receita errada. O modelo deve usar `null` quando não houver a informação requerida, em vez de inventá-la.

!!! warning "Uma confusão frequente"
    A margem operacional é resultado operacional dividido por receita líquida. No relatório fictício de 2026-T2, \(165/1000=16{,}5\%\). A margem líquida é \(107/1000=10{,}7\%\). As duas razões não medem a mesma coisa.

## 4. Critério de qualidade

Uma extração só pode ser considerada confiável depois de conferidos: documento de origem, período, unidade e regra para valores ausentes. Repetir o prompt até obter uma resposta agradável não é um método de avaliação. Em laboratório, o texto será curto e sintético para que todos possam fazer a conferência manual.


## Laboratório interativo

Antes de realizar a atividade, **registre um palpite**. Depois altere os parâmetros, observe a resposta e explique a divergência. O simulador executa operações locais: não inventa acesso a dados nem faz chamadas a um LLM real.

<div class="sim-shell"><iframe src="../../assets/simuladores/laboratorio.html?modulo=3" title="Laboratório interativo da aula 3" loading="lazy"></iframe></div>

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

1. Especificar o esquema de campos com tipos e valores nulos.
2. Testar uma resposta com JSON válido e números incorretos.
3. Extrair receita e lucro de um relatório fictício e conferir a margem em código.

**Produto da aula:** Extrator de informações financeiras com esquema e política de campos ausentes.

## Exercício para a semana

Entregue no Blackboard, individualmente, **um registro conciso** (até duas páginas ou notebook com comentários) que documente: (a) a pergunta e o método; (b) os dados utilizados, seus períodos e unidades; (c) dois resultados reproduzíveis; (d) pelo menos uma limitação; (e) uma verificação independente de uma conclusão produzida com IA. O arquivo será mantido para documentação, **sem nota própria**. Os conceitos serão avaliados no quiz seguinte.

## Para conferir a compreensão

**Pergunta central:** Uma saída satisfaz todos os tipos do JSON Schema. Isso prova que os números são verdadeiros?

Responda sem utilizar o simulador. A solução comentada será retomada no quiz correspondente. Não memorize comandos: explique o conceito e o motivo da escolha.

---

<div class="lesson-footnav"><a href="../02-embeddings-e-concorrencia/">← Anterior</a><a href="../04-classificacao-e-avaliacao/">Próximo →</a></div>
