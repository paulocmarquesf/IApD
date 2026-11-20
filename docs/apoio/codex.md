# Desenvolvimento com Codex

O aluno utiliza **somente a interface gráfica** do Codex. O curso não requer utilização de terminal ou escrita manual de código.

## Sequência sugerida de prompts

1. **Especificação:** descreva entrada, saída, casos de exceção e critérios de aceitação.
2. **Implementação:** solicite ao Codex que crie a aplicação e os testes a partir da especificação.
3. **Execução:** peça que execute os testes e apresente saídas observáveis.
4. **Auditoria:** confronte os resultados com exemplos manuais e inspecione situações não respondíveis.
5. **Correção:** descreva a falha e peça uma alteração mínima com regressão dos testes.
6. **Depósito:** solicite ao Codex que organize os arquivos para envio ao repositório individual no GitHub; confira a publicação pela interface gráfica.

Quando a aplicação necessitar de geração ou interpretação de linguagem, seu código Python pode utilizar `openai_codex` em segundo plano. Essa alternativa precisa ser pilotada quanto a autenticação ChatGPT Edu, permissões, limites e latência. Não se deve apresentar como comprovada uma capacidade ainda não testada nas máquinas da instituição. O Codex Python SDK opera sessões de agente e não é um substituto idêntico da API convencional de inferência.

## Laboratório complementar opcional

[Comparação entre Codex SDK e API convencional](api-complementar.md): a mesma triagem de mensagens pode ser projetada com duas infraestruturas, sem depender dessa atividade no percurso obrigatório.
