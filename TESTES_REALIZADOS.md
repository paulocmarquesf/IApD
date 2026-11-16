# Verificações realizadas nesta entrega

- **Estrutura:** `python scripts/verificar_repositorio.py` aprovado (12 aulas, 12 notebooks, links locais e arquivos docentes separados de `docs/`).
- **Conceitos e cálculos:** `python -m pytest -q tests` aprovado (5 testes).
- **Simuladores:** arquivo JavaScript validado por `node --check docs/assets/simuladores/laboratorio.js`.
- **Notebooks:** aulas 01 a 07 aprovadas em execução consecutiva; aula 08 aprovada isoladamente; aulas 09 a 12 aprovadas isoladamente com kernel Python e `nbclient`. Uma tentativa adicional de execução dos 12 em um único processo foi interrompida por limite de tempo/instabilidade de kernel da sessão, não por falha identificada no conteúdo.
- **Zensical:** configuração TOML validada e links internos conferidos; **não foi possível executar `zensical build` nesta sessão** porque a ferramenta não está instalada e a instalação pelo pip não tem acesso à rede.
- **Para homologação final:** em ambiente com internet, `python -m pip install -r requirements-site.txt`, `zensical build --clean`, `zensical serve`; conferir links e tema no navegador. Depois instalar requisitos de laboratório e rodar os scripts do README. Testar os arquivos de importação no Blackboard e o Smowl com uma turma piloto antes de uso real.

## Escopo e fidelidade

O curso usa **somente a segunda parte** (LLMs, embeddings, componentes, ferramentas, RAG, avaliação, agentes e segurança) como referência curricular. Não contém as aulas de fundamentos de ML da Parte A. Os exemplos e textos são independentes e usam **dados sintéticos ou documentos claramente ficcionais**, que não substituem séries oficiais, atas do Copom ou demonstrativos reais. Gabaritos e questões sigilosas estão em `docente_privado/` e devem ser removidos antes de publicar o repositório em GitHub público.
