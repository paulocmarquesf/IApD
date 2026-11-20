# Aula 10 — Exercícios conceituais

**Resolução individual em papel.** Mostre as contas intermediárias e explicite as hipóteses.

### Exercício 10.1 Melhoria líquida e regressões

Em 40 atendimentos, a configuração A acerta 26. B corrige oito falhas de A, mas erra três casos antes corretos. Calcule acertos de B, taxas de A e B e ganho em pontos percentuais. Por que olhar somente a taxa de B esconde um risco operacional?

### Exercício 10.2 Ganho absoluto e relativo

A taxa de respostas fundamentadas cresce de 60% para 72%. Calcule (a) ganho em pontos percentuais; (b) crescimento relativo; (c) a quantidade de casos adicionais em 50 solicitações, admitindo as proporções como frequências observadas.

### Exercício 10.3 Duas mudanças simultâneas

Em uma versão foram alterados prompt, tamanho de chunk e modelo de embedding. A taxa de acerto cresceu. O aumento pode ser atribuído à mudança do prompt? Descreva um desenho de ablação mínimo que permita estudar o efeito de cada componente.

### Exercício 10.4 Uma melhora com custo de espera

Configuração A: 80% de acertos e latência mediana de 2 s; B: 88% e 11 s. O SLA exige resposta em até 5 s. Qual sistema atende ao SLA com base apenas na mediana informada? É possível concluir que todos os usuários de A tiveram menos de 5 s? Justifique.

### Exercício 10.5 Juiz automatizado complacente

Um avaliador de LLM marca como correta uma resposta com número falso, porque a redação é clara. Formule uma rubrica com três dimensões independentes e uma regra de reprovação para afirmações sem evidência documental.

### Exercício 10.6 Amostra pequena, grande anúncio

Em dez casos, a versão A acerta oito e B acerta nove. Um relatório anuncia “ganho comprovado de dez pontos percentuais”. Diferencie diferença amostral, evidência estatística e relevância prática. Que novos dados seriam desejáveis?

### Exercício 10.7: Pontos percentuais

Acertos sobem de 70/100 para 77/100. Calcule aumento em pontos percentuais e variação relativa.

### Exercício 10.8: Pareamento

Modelo A acerta casos 1-5; B acerta 2-6. Ambos fazem cinco acertos em seis casos. Por que inspecionar pares discordantes?

### Exercício 10.9: Custo versus qualidade

Um sistema ganha 1 ponto percentual, mas triplica latência. Proponha regra clara para decidir se a troca compensa.

### Exercício 10.10: Juiz inconsistente

Um avaliador automatizado prefere resposta longa mesmo quando inclui informação sem fonte. Como auditar seu critério?
