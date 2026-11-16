#!/usr/bin/env python3
"""Verificação de integridade do repositório Zensical, sem rede.
Saída não substitui `zensical build`, que requer a ferramenta instalada.
"""
from pathlib import Path
import json,re,sys,tomllib,csv,html.parser
R=Path(__file__).resolve().parents[1];D=R/'docs'
errs=[];stats={}
conf=tomllib.loads((R/'zensical.toml').read_text(encoding='utf8'))
assert conf['project']['site_name']=='Inteligência Artificial para Decisão'

def nav_entries(x):
 if isinstance(x,str):yield x
 elif isinstance(x,dict):
  for v in x.values():yield from nav_entries(v)
 elif isinstance(x,list):
  for v in x:yield from nav_entries(v)
for p in nav_entries(conf['project']['nav']):
 if not (D/p).exists():errs.append('nav não encontrado: '+p)
lessons=sorted((D/'aulas').glob('*/index.md'))
if len(lessons)!=12:errs.append('Esperadas 12 aulas, encontradas '+str(len(lessons)))
for ix,p in enumerate(lessons,1):
 folder=p.parent
 for req in ['index.md','aula.ipynb','opcionais.md','slides/aula.html']:
  if not (folder/req).exists():errs.append('aula sem recurso: '+str(folder/req))
 nb=json.loads((folder/'aula.ipynb').read_text(encoding='utf8'))
 if not nb.get('cells'):errs.append('notebook vazio: '+str(folder))
 for j,c in enumerate(nb['cells']):
  if c['cell_type']=='code':
   try:compile(''.join(c['source']),str(folder), 'exec')
   except SyntaxError as ex:errs.append(f'notebook erro: aula {ix}, cel {j}: {ex}')
 if f'modulo={ix}' not in p.read_text(encoding='utf8'):errs.append('iframe com ID errado: '+str(folder))

# Markdown link checking; raw HTML paths must point to existing docs and should not end in .md
class Hrefs(html.parser.HTMLParser):
 def __init__(self):super().__init__();self.hrefs=[]
 def handle_starttag(self,tag,attrs):
  if tag in ('a','iframe','script','link'):
   dd=dict(attrs)
   for key in ('href','src'):
    if key in dd:self.hrefs.append((tag,dd[key]))
md_pat=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
for p in D.rglob('*.md'):
 text=p.read_text(encoding='utf8');parser=Hrefs();parser.feed(text)
 urls=[(tag,url) for tag,url in parser.hrefs]+[('markdown',u) for u in md_pat.findall(text)]
 for tag,url in urls:
  url=url.split('#',1)[0].split('?',1)[0]
  if not url or url.startswith(('https://','http://','mailto:','javascript:','data:','//')):continue
  if url.startswith('/'):
   errs.append('URL absoluta local (arriscada para subdiretório): '+str(p)+': '+url);continue
  target=(p.parent/url).resolve()
  if tag=='a' and url.endswith('.md'):
   errs.append(f'HTML link para .md não será reescrito pelo Zensical: {p}: {url}')
  if target.is_dir():target=target/'index.md'
  if not target.exists() and url.endswith('/'):target=(p.parent/url.rstrip('/')).with_suffix('.md')
  if not target.exists():errs.append('link quebrado: '+str(p.relative_to(D))+': '+url)

for path in [D/'caderno'/'caderno.pdf',D/'caderno'/'atividades.md',R/'docente_privado'/'gabarito-caderno.pdf',R/'docente_privado'/'PI-modelo-blackboard.txt',R/'docente_privado'/'PF-modelo-blackboard.txt']:
 if not path.exists() or path.stat().st_size<100:errs.append('artefato ausente: '+str(path))
for i in range(1,12):
 p=R/'docente_privado'/'quizzes'/f'quiz-{i:02d}-blackboard.txt'
 if not p.exists():errs.append('quiz faltando: '+str(p))
 elif len(p.read_text(encoding='utf-8-sig').splitlines())!=5:errs.append('quiz deve conter cinco questões: '+str(p))
 else:
  for l in p.read_text(encoding='utf-8-sig').splitlines():
   fields=l.split('\t')
   if len(fields)!=10 or fields[0]!='MC' or fields.count('correct')!=1 or fields.count('incorrect')!=3:errs.append('quiz formato inválido: '+str(p))

# Não incluir a parte de ML convencional do curso de referência.
if (D/'ml').exists() or (D/'2027.1'/'classes'/'1a-problema-de-ml').exists():errs.append('foi incluída parte A de ML da referência')

print(f'Arquivos: {len(list(R.rglob("*")))} | aulas: {len(lessons)} | PDFs: {len(list(R.rglob("*.pdf")))} | notebooks: {len(list(R.rglob("*.ipynb")))}')
print('Site: Zensical TOML parseou; nav e links locais verificados; material docente fora de docs/.')
if errs:
 print('\n'.join('ERRO: '+m for m in errs));sys.exit(1)
print('VERIFICAÇÃO ESTÁTICA: APROVADA')
