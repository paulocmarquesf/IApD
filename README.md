# Inteligência Artificial para Decisão

**Curso para graduação em Economia e Administração — 12 aulas de 2 horas + PI + PF.**

Um repositório Zensical completo, autoral, com exemplos em Marketing Analítico, Finanças básicas e Macroeconomia básica. Conteúdo principal: LLMs, embeddings, estruturação de respostas, classificação, ferramentas, aplicações compostas, RAG, avaliação, agentes e segurança.

## Executar o site (Windows, PowerShell)

```powershell
cd curso_ia_decisao_zensical
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-site.txt
zensical serve
```

Abra http://127.0.0.1:8000. Em Linux/macOS, ative o ambiente com `source .venv/bin/activate`.

Para gerar o site estático:

```powershell
zensical build --clean
python -m http.server 8000 --directory site
```

O HTML gerado fica em `site/`. Nunca abra o arquivo Markdown diretamente e espere que a navegação apareça: **o Zensical precisa compilar o site**. A aplicação de laboratório tem HTML/JS próprio e funciona sem API.

## Notebooks e código

```powershell
python -m pip install -e .
python -m pip install -r requirements-labs.txt
jupyter lab
```

Os notebooks de cada aula estão em `docs/aulas/<slug>/aula.ipynb`. Todos os **12 notebooks básicos** funcionam localmente e não precisam de OpenAI nem de GPU. Experimentos com LLMs ou LangGraph estão em `exemplos/` e exigem instalação extra; consulte `exemplos/README.md`. Não comprometa nem publique chaves.

## Testar

```powershell
python -m pip install -e ".[tests]"
python -m pytest tests -q
python scripts/verificar_repositorio.py
python scripts/testar_notebooks.py
```

`scripts/verificar_repositorio.py` verifica TOML, aulas, notebooks, slides, arquivos referenciados e estrutura. `scripts/testar_notebooks.py` executa os notebooks em ambiente local, sem APIs. O build de Zensical faz parte do CI GitHub Actions e deve ser verificado na máquina do usuário se a ferramenta não estiver disponível na máquina de desenvolvimento.

## Materiais

- `docs/`: site público, programa, 12 aulas, slides HTML, simuladores, caderno, orientação das avaliações e casos.
- `dados/`: bases **totalmente fictícias/sintéticas**, documentos e perguntas de referência.
- `src/iad/`: cálculos, métricas, índices de busca e workflow auditáveis.
- `docente_privado/`: **material reservado**, banco de questões com gabaritos, PI e PF; não faz parte do site publicado.
- `exemplos/`: integrações opcionais com LLM API, Chroma, LangChain e LangGraph.
- `scripts/`: geradores, testes e verificações.

### Importante sobre privacidade do professor

O conteúdo de `docente_privado/` está no ZIP para facilitar o trabalho. **Se publicar o repositório como público no GitHub, remova esta pasta do histórico do Git antes de publicar**. O fato de ela estar fora de `docs/` impede a publicação no site, mas não impede acesso pelo repositório público. Alternativamente, mantenha o projeto privado e publique apenas o site.

## Estrutura de avaliação

Onze quizzes (aplicados nas aulas 2–12, sobre a aula anterior), uma PI (após aula 6) e uma PF (após aula 12). Pesos sugeridos: 20%, 35% e 45%, respectivamente. Os trabalhos individuais semanais são registrados no Blackboard sem nota de artefato. Configurações específicas de Blackboard e Smowl devem ser homologadas institucionalmente.

## Fonte de inspiração

A organização conceitual e a ideia de aulas com simuladores, slides, notebooks, caderno e notas docentes foram inspiradas na **Parte B do curso de Inteligência Artificial da Engenharia de Computação e Mecânica do Insper** (https://insper.github.io/AI/), edição 2027.1. **As exposições, casos, código, gráficos, simuladores e avaliações deste repositório foram escritos de forma independente** para ECO/ADM. Não foram copiados textos, slides, imagens, simuladores ou códigos daquele curso. Os casos de Marketing remetem à tradição de problemas de *Data Science, Marketing & Business* (Fernandez e Marques).

**Dados:** os nomes Horizonte Comércio S.A. e Loja Aurora são fictícios; nenhuma tabela macroeconômica representa números oficiais. O material não oferece aconselhamento financeiro.
