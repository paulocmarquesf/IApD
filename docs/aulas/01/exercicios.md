# Aula 01 — Exercícios conceituais

**Resolução individual em papel.** Mostre as contas intermediárias e explicite as hipóteses.

### Exercício 1.1 A próxima palavra do comunicado

Um gerador deve completar a expressão “O prazo será”. Para os tokens “mantido”, “ampliado” e “revisto”, as probabilidades são 0,50, 0,35 e 0,15. (a) Indique a saída gulosa; (b) determine a chance de amostrar algo diferente de “mantido”; (c) explique por que repetir a geração pode produzir resultados distintos sem mudar os dados.

### Exercício 1.2 Duas etapas, uma notícia

Para o início “A empresa”, suponha $P(\text{reduziu}\mid\text{A empresa})=0{,}4$ e $P(\text{preços}\mid\text{A empresa reduziu})=0{,}6$. Calcule a probabilidade da sequência de dois tokens. Um colega multiplica 0,4 pela frequência incondicional da palavra “preços”, igual a 0,3. Identifique seu erro.

### Exercício 1.3 Atenção numa reclamação

Três trechos de uma reclamação recebem pesos não normalizados 1, 2 e 5, associados a valores escalares 4, 1 e 3. Normalize os pesos e calcule a saída ponderada. O maior peso prova que o terceiro trecho foi a causa da insatisfação? Justifique.

### Exercício 1.4 Um orçamento de contexto

Uma janela comporta 12 tokens. Uma instrução ocupa 4, o histórico ocupa 5 e a nova pergunta ocupa 5. (a) Quantos tokens excedem a janela? (b) Descreva duas estratégias de redução; (c) explique por que eliminar os primeiros tokens indiscriminadamente pode alterar a interpretação.

### Exercício 1.5 O dado que não existia

A avaliação diz: “A bateria dura menos do que eu esperava; ainda não procurei suporte”. Um resumo afirma: “O cliente solicitou devolução, que foi negada pela empresa”. Separe (a) duas afirmações efetivamente sustentadas do (b) que foi inventado. Escreva uma alternativa fundamentada.

### Exercício 1.6 Um token não é uma palavra

Dois tokenizadores codificam “reembolso imediato”: T1 usa 2 tokens e T2 usa 5 tokens. Para 800 ocorrências independentes dessa expressão, quantos tokens cada um consumiria apenas nesse trecho? Qual informação adicional seria necessária para estimar o total do documento?

### Exercício 1.7: Evidência e inferência

A sentença “o suporte não me retornou” sustenta afirmar que o cliente abriu um chamado? Distinga ausência de resposta e ausência de informação sobre a abertura do chamado.

### Exercício 1.8: Dois prefixos

No prefixo A, uma continuação tem probabilidade 0,8; no prefixo B, 0,2. Se o prefixo for selecionado com probabilidades 0,3 e 0,7, calcule a probabilidade marginal da continuação.

### Exercício 1.9: Pesos de atenção

Uma combinação ponderada de valores (2, 6, 10) usa pesos (0,2; 0,3; 0,5). Calcule o resultado e diga se é correto chamá-lo de “interpretação do modelo”.

### Exercício 1.10: Teste de robustez

Uma avaliação diz “Não foi ruim, mas eu não compraria de novo”. Especifique uma pergunta de verificação e a evidência que impediria classificar automaticamente como elogio.
