# Folha de consulta conceitual

## Vetores e similaridade

Para vetores não nulos: `cos(u,v) = (u·v) / (||u|| ||v||)`.

## Avaliação de classificação

Acurácia = total de classificações corretas / total de casos. Falso negativo: referência positiva, previsão negativa.

## Risco de carteira

Retorno esperado = soma ponderada dos retornos. Variância = `wᵀΣw`. Índice de Sharpe = `(E[R] − r_f)/σ` sob frequências compatíveis.

## Recuperação

Hit@k = proporção das perguntas com ao menos um relevante nas primeiras k posições. MRR@k = média de `1/r`, onde r é o posto do primeiro relevante e a contribuição é zero se r>k.

## Comparação controlada

Registrar casos que melhoraram, pioraram e permaneceram iguais; manter conjunto e critérios constantes.

## Confiabilidade

Sob independência e probabilidade constante p: `pass@k = 1 − (1−p)^k`; `pass^k = p^k`.

## Segurança

A autoridade de um texto externo é diferente da autorização de uma ferramenta. A ação sensível exige validação de permissão fora do prompt.
