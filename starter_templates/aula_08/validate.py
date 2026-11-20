from pathlib import Path
import sys
expected=['dialogos.md', 'fontes.csv', 'interpretacao.md', 'testes.json']
missing=[p for p in expected if not Path(p).is_file() or Path(p).stat().st_size==0]
if missing:
    print("Arquivos ausentes ou vazios:",missing)
    sys.exit(1)
print("Presença de arquivos verificada. Não equivale a correção semântica.")
