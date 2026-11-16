<div class="lesson-kicker">AULA 05 <span>·</span> MARKETING E FINANÇAS <span>·</span> 120 MINUTOS</div>

# Ferramentas: quando o LLM deve calcular

<p class="lesson-lede">Por que o assistente deve chamar uma função para calcular margens, retorno e variação percentual?</p>

<div class="case-strip"><span class="case-label">O problema</span>Uma equipe pede ao assistente para comparar o retorno atribuído de campanhas e a margem operacional de uma empresa.</div>

!!! abstract "Resultados de aprendizagem"
    - **1.** Tool calling e parâmetros.
    - **2.** Separação entre linguagem e cálculo.
    - **3.** Funções determinísticas e unidades.
    - **4.** Validação de entradas e testes.

<div class="lesson-actions"><a href="aula.ipynb" download>↓ Notebook guiado</a><a href="slides/aula.html" target="_blank">▣ Slides</a><a href="opcionais/">+ Ampliação</a></div>

<div class="lesson-mini">Conceitos · tool calling e parâmetros, separação entre linguagem e cálculo, funções determinísticas e unidades, validação de entradas e testes</div>

---


## 1. Falar sobre uma conta não é fazê-la

O LLM pode traduzir uma solicitação de linguagem natural em uma chamada para uma função programada. A ferramenta recebe parâmetros explícitos, executa a operação e devolve um resultado. A tarefa do modelo é decidir **qual função utilizar**, preencher os argumentos e explicar o retorno em linguagem acessível.

Esse desenho separa três responsabilidades: a interpretação da pergunta, o cálculo e a apresentação do resultado. A precisão do cálculo depende da implementação e da qualidade dos dados; a adequação da explicação depende também do modelo.

## 2. O contrato da ferramenta

```python
def retorno_sobre_custo(receita_atribuida: float, custo: float) -> float:
    if custo <= 0:
        raise ValueError("custo deve ser positivo")
    return (receita_atribuida - custo) / custo
```

A função não precisa saber o nome da campanha, o setor ou a data. Ela precisa de dois valores expressos **na mesma moeda e no mesmo período**. Sua saída é uma razão, não uma porcentagem formatada. O modelo deve apresentar `0.5` como 50%, não como 0,5%.

## 3. Retorno atribuído não é efeito causal

Uma campanha gastou R$ 8 mil e teve R$ 12 mil de receita atribuída. O indicador de receita menos custo sobre custo é 50%. O cálculo está correto **sob a definição informada**. Não sabemos, entretanto, quanto da receita teria ocorrido sem a campanha; portanto, o indicador não mede necessariamente retorno incremental. A diferença entre atribuição e causalidade aparece mesmo em exemplos elementares.

## 4. Finanças com poucos conceitos

No relatório fictício da Horizonte, receita líquida e resultado operacional permitem calcular margem operacional. Duas ferramentas simples, `margem(operacional, receita)` e `variacao_percentual(valor_atual, anterior)`, podem apoiar a interpretação. A ferramenta deve recusar denominador zero e validar períodos comparáveis.

!!! tip "Regras para uso seguro"
    Se a entrada tem unidade ambígua, o assistente deve solicitar esclarecimento. Se não há fonte, não deve atribuir o cálculo a um balanço real. Se a ferramenta falhar, a resposta deve mostrar a falha e não inventar a saída.


## Laboratório interativo

Antes de realizar a atividade, **registre um palpite**. Depois altere os parâmetros, observe a resposta e explique a divergência. O simulador executa operações locais: não inventa acesso a dados nem faz chamadas a um LLM real.

<div class="sim-shell"><iframe src="../../assets/simuladores/laboratorio.html?modulo=5" title="Laboratório interativo da aula 5" loading="lazy"></iframe></div>

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

1. Desenhar o contrato de uma ferramenta com seus argumentos.
2. Executar cálculos com a ferramenta local e conferir manualmente.
3. Identificar a afirmação causal indevida sobre receita atribuída a campanhas.

**Produto da aula:** Calculadora financeira e de campanhas acionada por perguntas em linguagem natural.

## Exercício para a semana

Entregue no Blackboard, individualmente, **um registro conciso** (até duas páginas ou notebook com comentários) que documente: (a) a pergunta e o método; (b) os dados utilizados, seus períodos e unidades; (c) dois resultados reproduzíveis; (d) pelo menos uma limitação; (e) uma verificação independente de uma conclusão produzida com IA. O arquivo será mantido para documentação, **sem nota própria**. Os conceitos serão avaliados no quiz seguinte.

## Para conferir a compreensão

**Pergunta central:** Uma campanha gastou R$ 8 mil e teve receita atribuída de R$ 12 mil. Qual é (receita−custo)/custo?

Responda sem utilizar o simulador. A solução comentada será retomada no quiz correspondente. Não memorize comandos: explique o conceito e o motivo da escolha.

---

<div class="lesson-footnav"><a href="../04-classificacao-e-avaliacao/">← Anterior</a><a href="../06-aplicacoes-compostas/">Próximo →</a></div>
