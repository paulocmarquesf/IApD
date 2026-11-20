# Aula 04 — Exercícios conceituais

**Resolução individual em papel.** Mostre as contas intermediárias e explicite as hipóteses.

### Exercício 4.1 Uma triagem que ignora urgências

Em 50 mensagens, a classe “urgente” produz $\text{TP}=8$, $\text{FP}=4$, $\text{FN}=12$, $\text{TN}=26$. Calcule precision, recall e accuracy. A empresa tolera mais falsos positivos do que falsos negativos: qual métrica merece maior atenção?

### Exercício 4.2 Perdas assimétricas

Para o classificador A, $\text{FP}=6$ e $\text{FN}=2$; para B, $\text{FP}=2$ e $\text{FN}=4$. Cada falso positivo custa 1 unidade e cada falso negativo custa 5. Calcule as duas perdas totais e indique qual sistema é preferível por esse critério.

### Exercício 4.3 A ilusão da classe majoritária

Um golden set contém 90 mensagens rotuladas “comum” e 10 “urgente”. Um classificador diz sempre “comum”. Determine a accuracy e o recall para “urgente”. Por que a accuracy alta não é uma boa notícia?

### Exercício 4.4 Rótulos sob disputa

Dois avaliadores discordam sobre uma mensagem: um classifica como “troca” e outro como “devolução”; a taxonomia não define a diferença. Qual parte do sistema deve ser corrigida primeiro: o prompt, o rótulo de referência ou a própria taxonomia? Proponha procedimento justificável.

### Exercício 4.5 Conjunto de teste contaminado

Um estudante altera o prompt cinco vezes, observando em cada rodada os mesmos 20 casos de avaliação, e apresenta a melhor pontuação como resultado final. Explique o viés produzido e descreva uma separação mínima entre desenvolvimento e avaliação final.

### Exercício 4.6 Dois erros de tipos diferentes

Em 30 respostas, 3 falharam no schema e 5 eram estruturalmente válidas, mas tinham categoria errada; nenhum caso pertence aos dois grupos. Calcule a taxa de respostas simultaneamente válidas e corretas. Explique por que as duas falhas exigem reparos diferentes.

### Exercício 4.7: Ganhar accuracy, perder recall

Uma população tem 95 negativos e 5 positivos. Compare dois classificadores: A prevê tudo negativo; B detecta 4 positivos mas gera 8 falsos positivos. Calcule accuracy e recall.

### Exercício 4.8: Perda de operação

Modelo A tem 4 FN e 10 FP; B tem 7 FN e 2 FP. Se o custo de FN é 4 e FP é 1, compare as perdas.

### Exercício 4.9: Acordo de anotadores

Dois especialistas concordam em 42 das 50 mensagens. Calcule a proporção de concordância e explique por que ela não substitui uma regra de rotulagem.

### Exercício 4.10: Recuperação de erro

Uma mudança de prompt eliminou três falhas de JSON, mas criou duas classificações erradas. Como comparar as versões sem misturar tipos de erros?
