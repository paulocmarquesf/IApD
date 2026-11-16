#!/usr/bin/env python3
"""Executa os 12 notebooks em kernel real; falha no primeiro erro."""
from pathlib import Path
import sys,time
import nbformat
from nbclient import NotebookClient
ROOT=Path(__file__).resolve().parents[1]
paths=sorted((ROOT/'docs'/'aulas').glob('*/aula.ipynb'))
if len(paths)!=12:raise RuntimeError('Esperados 12 notebooks')
for i,p in enumerate(paths,1):
 nb=nbformat.read(str(p),as_version=4)
 start=time.monotonic()
 print(f'[{i:02d}/12] {p.parent.name}',flush=True)
 try:
  cli=NotebookClient(nb,timeout=100,kernel_name='python3',resources={'metadata':{'path':str(ROOT)}})
  cli.execute()
 except Exception as exc:
  print(f'ERRO: {p}: {exc}',file=sys.stderr)
  raise
 errors=[(idx,output) for idx,cell in enumerate(nb.cells) if cell.cell_type=='code' for output in cell.get('outputs',[]) if output.output_type=='error']
 if errors:raise RuntimeError(f'Erro no notebook {i}: {errors}')
 print(f'       OK ({time.monotonic()-start:.1f}s, {len(nb.cells)} células)',flush=True)
print('12 NOTEBOOKS: EXECUTADOS COM SUCESSO')
