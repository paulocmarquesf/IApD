# Aula 05 — Exercícios conceituais

**Resolução individual em papel.** Mostre as contas intermediárias e explicite as hipóteses.

### Exercício 5.1 Retorno simples e datas

Uma cota vale R\$ 100 no início, R\$ 105 no fim do período 1 e R\$ 102,90 no fim do período 2. Calcule os retornos simples de cada período e o retorno acumulado. Por que somar retornos simples pode produzir um valor incorreto?

### Exercício 5.2 Diversificação não é média das volatilidades

Uma carteira combina dois ativos com pesos $w_A=0{,}6$ e $w_B=0{,}4$, volatilidades 20% e 10% e correlação 0,25. Calcule a variância da carteira e sua volatilidade. Compare com $0{,}6(20\%)+0{,}4(10\%)$.

### Exercício 5.3 Carteira A ou B?

Carteira A: retorno esperado 8%, volatilidade 12%; carteira B: 10%, volatilidade 20%. Com taxa livre de risco de 2%, calcule o índice de Sharpe de cada uma. A carteira de maior retorno é necessariamente a de maior Sharpe?

### Exercício 5.4 A ferramenta que nunca foi chamada

Um assistente relata “calculei a covariância = 0,012”, mas o log contém apenas leitura de preços. Qual evidência falta para sustentar o cálculo? Especifique entrada, função e saída que deveriam constar de um rastro auditável.

### Exercício 5.5 Um erro de unidade

Um retorno mensal médio é 1% e um aluno o compara diretamente com uma taxa livre de risco anual de 6% no cálculo do Sharpe. Identifique o problema de comparabilidade e explique o que deve ser convertido antes da comparação.

### Exercício 5.6 Ação dominante?

Dois ativos têm mesmo retorno esperado, mas o segundo possui maior volatilidade. Podemos concluir que o primeiro domina o segundo em qualquer carteira possível? Discuta o papel das covariâncias com os demais ativos e a diferença entre analisar um ativo isolado e uma carteira.

### Exercício 5.7: Correlação e risco

Duas carteiras têm os mesmos pesos e volatilidades marginais, mas correlações -1 e +1. Explique a diferença de risco usando a fórmula da variância.

### Exercício 5.8: Duas chamadas de ferramenta

O rastro mostra calcular_retorno com entrada mensal e calcular_sharpe com r_f anual. Localize a incompatibilidade.

### Exercício 5.9: Carteira inviável

Otimização impõe soma de pesos igual a 1 e retorno mínimo 20%, enquanto todos os ativos têm retorno esperado inferior a 10% e não se permite alavancagem. É possível?

### Exercício 5.10: Validar preço ajustado

Um dado de cotação cai 50% exatamente após desdobramento 2:1. Que informação precisa ser checada antes de interpretar o retorno?
