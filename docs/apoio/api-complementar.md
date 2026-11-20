# Laboratório opcional: integração por API convencional

**Não integra as atividades obrigatórias.** O objetivo é comparar dois mecanismos de integração com modelos de linguagem usando o caso de triagem estruturada da Aula 3.

## Duas arquiteturas

- **Percurso principal:** interface gráfica do Codex desenvolve a aplicação; a geração em execução pode utilizar o Codex Python SDK, mediante autenticação institucional validada.
- **Percurso alternativo:** a aplicação utiliza o SDK da API convencional da OpenAI, com chave institucional fornecida em ambiente apropriado e controle de consumo.

## Atividade

Solicite ao Codex que produza, a partir da mesma especificação de triagem, duas versões de integração. Compare formato da resposta, tratamento de ausência de dados, latência, custo por operação, rastreabilidade e limites de operação. Não publique chaves em arquivos nem em repositórios.

**Questões:** Que diferenças vêm da infraestrutura e quais vêm do prompt? As saídas cumprem o mesmo esquema? Como a comparação deve controlar variabilidade e exposição de dados?
