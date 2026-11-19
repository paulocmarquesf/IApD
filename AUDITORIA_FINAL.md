# Auditoria final do curso

**Curso:** Inteligência Artificial para Decisão  
**Instituição:** Insper  
**Docente:** Paulo C. Marques F.  
**Data:** 19 de novembro de 2026

## Materiais conferidos

| Material | Quantidade | Situação |
|---|---:|---|
| Páginas completas de aula | 12 | Presentes e vinculadas à navegação |
| Apresentações HTML | 12 × 14 telas | Presentes, com identidade institucional e navegação por teclas |
| Quizzes conceituais | 12 × 4 questões | Com alternativas, gabarito e explicações |
| Quizzes sobre atividades domiciliares | 11 × 4 questões | Na abertura das aulas 2 a 12 |
| Notebooks Jupyter | 12 | Executados localmente sem erro |
| Simuladores interativos | 12 | Inicialização testada em JavaScript |
| Diagramas SVG | 12 | Arquivos e links verificados |
| Caderno de atividades | 1 PDF de 12 páginas + versão web | Conferido |
| Handouts de tarefas domiciliares | 12 | Um por aula, com novos cenários e roteiro de entrega |
| Laboratórios práticos | 12 | Um por aula; desenvolvimento 100% por prompts |
| Projetos acompanhados | 3 progressivos + 2 independentes | Conexões descritas nas aulas |
| Provas-modelo | 2 PDFs (PI e PF) | Questões conceituais, 100 pontos cada |
| Gabaritos das provas | 2 PDFs e 2 arquivos Markdown | Em pasta não publicada |
| Bibliografia e fontes | 1 seleção + fontes públicas | Selecionadas e identificadas |
| Dados e documentos didáticos | 16 arquivos | Sintéticos, com origem documentada |
| Materiais de apoio ao estudo | Mapa, folha, glossário, simuladores | Publicados |
| Orientações e soluções docentes | 12 planos, 12 handouts resolvidos, provas, caderno, banco de quizzes | Fora de `docs/`, ignorados pelo Git |
| Aplicações de referência | 4 demonstradores locais + 2 modelos de integração | Executadas sem serviços remotos onde aplicável |

**Tutor de IA não incluído**, conforme definido para esta edição.

## Testes realizados

- Estrutura, arquivos, links internos e PDFs: **1.903 verificações, nenhuma falha**.
- JavaScript: validação sintática de três módulos e **53 scripts embutidos**.
- Inicialização dos simuladores e quizzes: **24 testes, nenhuma falha**.
- Controle de acesso em JavaScript: rejeição da senha incorreta e aceitação de `inspirar`/`pertencer` testadas.
- **12 notebooks executados**, utilizando os dados entregues, sem erros de execução.
- **Quatro aplicações locais de referência executadas**.
- Prova intermediária: duas páginas; prova final: duas páginas; caderno de atividades: 12 páginas. Gabaritos em PDF inspecionados.
- Conteúdo reservado fora de `site/` e pasta `docente_privado/` no `.gitignore`.
- Identidade visual com o vermelho `#E50505`, logotipo Insper e nome oficial do docente.

## Limites e verificações na publicação

1. **Compilação oficial do Zensical não executada neste ambiente:** o pacote não pôde ser instalado, pois o acesso à distribuição de dependências está bloqueado. O ZIP inclui `zensical.toml`, fontes em `docs/`, prévia estática funcional em `site/` e workflow de compilação/publicação. A compilação oficial deve ser conferida no primeiro push, pela aba Actions do repositório.
2. **Navegação e controles em navegador real:** a execução gráfica automatizada foi bloqueada pela política deste ambiente. A auditoria executou testes estáticos, de JavaScript e de componentes simulados. Testar no navegador após extrair o ZIP.
3. **Acesso por senha:** o bloqueio é exclusivamente client-side, em JavaScript. Não oferece confidencialidade; qualquer pessoa com acesso aos arquivos do repositório pode ler as credenciais e o conteúdo.
4. **API do ChatGPT Edu:** é necessário confirmar permissões, créditos e autenticação institucionais. O Codex CLI/SDK não equivale automaticamente a uma API de baixa latência para atender usuários finais. As demos locais funcionam sem credenciais.
5. **Dados de política monetária e investimentos:** os arquivos distribuídos são exemplos sintéticos identificados; atas e documentos oficiais são indicados por links e podem ser importados nas práticas.
6. **Substituição de repositório:** extrair sobre a pasta antiga **não remove arquivos obsoletos**. Recomenda-se substituir todos os arquivos antigos, preservando apenas `.git/`, antes de sincronizar.
7. **Privacidade dos gabaritos:** não sincronizar `docente_privado/`. A presença no `.gitignore` não remove arquivos que já eram rastreados pelo Git.

## Teste local recomendado

A partir da raiz do repositório, execute `python -m http.server 8000 --directory site` e abra `http://localhost:8000`. Após confirmar a interface, pressione `Ctrl+C`. Para publicar a versão Zensical, execute `zensical build` e sincronize com GitHub. Para a auditoria local completa, use `python scripts/auditoria_completa.py` com as dependências de teste instaladas.
