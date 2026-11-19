# Inteligência Artificial para Decisão

**Insper — Paulo C. Marques F.**  
12 aulas · Economia e Administração · 4º semestre

## Substituir o site anterior

Este pacote foi organizado com `zensical.toml`, `docs/`, `site/`, `dados/`, `exemplos/`, `scripts/` e `.github/` **diretamente na raiz do ZIP**, sem uma pasta extra envolvendo o projeto.

1. Faça backup da pasta local atual e dos arquivos pessoais não versionados.
2. Extraia o ZIP na pasta raiz do repositório, substituindo os arquivos correspondentes.
3. Apague arquivos antigos que não existem no pacote novo. **Extrair sobrescrevendo não remove arquivos obsoletos.** Prefira substituir o conteúdo por completo, preservando apenas a pasta `.git/` do repositório.
4. Abra `site/index.html` ou sirva a pasta `site/` localmente para um teste inicial. Para o navegador tratar arquivos e quizzes corretamente, execute um servidor HTTP simples: `python -m http.server 8000 --directory site` e abra `http://localhost:8000`.
5. Quando o Zensical estiver instalado, rode `zensical build` para regenerar a publicação oficial.
6. Sincronize a pasta com GitHub. A automação `.github/workflows/deploy.yml` compila o site com Zensical e publica pelo GitHub Pages; **é necessário configurar o Pages para GitHub Actions no repositório**.

## Senha de entrada

A página de acesso utiliza um bloqueio simples de JavaScript, conforme definido para a disciplina. **Não há autenticação de servidor**: a senha e todo o material publicado podem ser descobertos ao inspecionar o código e os arquivos do site. Não use essa barreira para informações confidenciais, avaliações sigilosas ou dados pessoais.

## O que está incluído

- 12 páginas completas, 12 decks HTML, 12 notebooks Jupyter.
- 12 simuladores interativos e 12 diagramas SVG.
- Quizzes conceituais por aula e quizzes de abertura das aulas 2–12 sobre atividades domiciliares.
- 12 handouts, caderno de exercícios em Markdown e PDF, mapa de conceitos, folha de consulta e glossário.
- Exemplos de provas PI e PF em PDF; gabaritos completos e notas docentes em `docente_privado/`.
- Bases didáticas sintéticas de Marketing, Finanças, política monetária, fundos e atendimento.
- Exemplos das duas rotas de acesso a modelos: OpenAI API e Codex CLI/Python SDK.

`docente_privado/` está no ZIP para uso local, mas consta de `.gitignore` e **não deve ser publicado em um repositório aberto**. Se algum arquivo dessa pasta já estiver versionado no Git, é preciso removê-lo do índice antes da sincronização.

## Limites da verificação

O site estático em `site/` é uma prévia funcional gerada a partir das mesmas fontes em `docs/`. Para publicar com o visual oficial do Zensical, o workflow recompila `docs/`. Uma validação local do Zensical depende da instalação do pacote na máquina de publicação.

## Requisitos

- Python 3.10 ou superior e Zensical para compilar a versão oficial.
- Codex autenticado pelo acesso institucional, se disponível.
- A API de modelos exige credenciais e cobrança autorizadas separadamente, se essa rota for escolhida.

O aluno não precisa escrever nem alterar código manualmente.
