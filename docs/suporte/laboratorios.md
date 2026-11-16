# Preparação dos laboratórios

Há três níveis de execução. **Nível 1 (obrigatório):** simuladores do navegador, sem instalações nem chaves. **Nível 2 (obrigatório, assistido por IA):** notebooks de Python locais, que podem ser executados e modificados com ajuda de um assistente de programação. **Nível 3 (opcional):** chamadas a serviços de LLM e frameworks externos.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m pip install -r requirements-labs.txt
jupyter lab
```

Para testar o site, instale `requirements-site.txt` e execute `zensical serve` na raiz. Abra [a primeira aula](../aulas/01-llms-e-limites/index.md) e mova o controle de temperatura.

**Critério de integridade:** se um notebook não executar, registrar o erro exato. Nunca substituir silêncio por resultados fabricados. Materiais de um provedor externo exigem consentimento institucional, credenciais apropriadas e atenção a custos e privacidade.
