# Codex: API e linha de comando

As aplicações da disciplina serão produzidas inteiramente com o Codex, usando uma licença institucional quando disponível. **O acesso ao ChatGPT Edu não implica automaticamente créditos para chamadas de API realizadas por aplicativos Python.** A instituição precisa confirmar limites e credenciais.

## Rota A — API de modelos na aplicação

Esta rota usa o SDK Python `openai` com uma variável de ambiente `OPENAI_API_KEY` fornecida por quem administra o projeto. O Codex escreve a integração e os testes; o aluno não digita código. Uma aplicação pode responder interativamente e executar chamadas durante o uso. A cobrança, o controle e o acesso da API pertencem à plataforma de API, conforme o contrato institucional.

**Prompt ao Codex:**

> Prepare o projeto para executar chamadas de modelo pelo SDK Python da OpenAI. Leia credenciais apenas de variáveis de ambiente. Não inclua chaves no código, no navegador nem no repositório. Implemente testes determinísticos, tratamento de erros, limites de chamadas e relatório de consumo quando disponível. Não execute chamadas pagas antes de receber minha autorização.

## Rota B — Codex CLI ou SDK Python do Codex

O Codex CLI permite trabalhar na pasta por instruções em linguagem natural. O SDK Python oficial `openai-codex` permite executar threads do Codex programaticamente, reutilizando autenticação da ferramenta, quando autorizada. É especialmente apropriado para **geração em lote, experimentos supervisionados e manutenção de projetos**. A capacidade de construir o aplicativo não implica que ele tenha um servidor de inferência disponível para responder continuamente a usuários externos.

**Prompt ao Codex:**

> Abra o projeto, execute o experimento da aula sobre o conjunto de dados local, salve as respostas em JSON e produza uma tabela de avaliação. Utilize sua sessão autenticada do Codex. Não armazene credenciais e não faça chamadas externas desnecessárias. Gere todos os arquivos e execute os testes; não peça ao aluno para editar código.

### Exemplo técnico disponível para inspeção

Os arquivos `exemplos/rota_api.py` e `exemplos/rota_codex_sdk.py` documentam as interfaces. Eles são **referências para o Codex executar ou adaptar**, não exercícios de escrita manual de Python.

O SDK Python do Codex não deve ser confundido com o SDK Python da API de modelos:

| Característica | API de modelos | Codex CLI / SDK |
|---|---|---|
| Autenticação | Chave de API institucional | Sessão Codex ou credenciais próprias |
| Uso típico | Inferência durante a execução da aplicação | Desenvolvimento e tarefas supervisionadas, inclusive em lotes |
| Interface Python | `openai` | `openai_codex` |
| Cobrança | Regras da API | Regras da sessão Codex/ChatGPT ou API, conforme login |
| Testes sem credenciais | Usar demonstrações determinísticas | Usar demonstrações determinísticas |

## Execução local sem credenciais

Cada aula dispõe de um simulador no navegador e um notebook com exemplo mínimo reprodutível. Eles não dependem de autenticação em serviços externos e permitem conferir o mecanismo central.

## Requisitos de segurança

Nunca colocar segredos em JavaScript público, notebooks distribuídos ou GitHub. Não executar ações financeiras reais, modificações em clientes ou envios de dados pessoais. Mensagens externas e documentos recuperados devem ser tratados como dados de autoridade inferior às instruções de controle.

## Documentação técnica

- [Codex Python SDK](https://github.com/openai/codex/tree/main/sdk/python)
- [Codex e ChatGPT](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)
- [API da OpenAI](https://platform.openai.com/docs/overview)
