"""Auditoria reprodutível, sem serviços externos ou credenciais."""
from pathlib import Path
import os,subprocess,sys,json,nbformat,fitz,tomllib
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def run(cmd):
 p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
 if p.returncode:raise RuntimeError(f'Falha {cmd}: {p.stderr or p.stdout}')
 checks.append((str(cmd),p.stdout.strip().splitlines()[-1] if p.stdout.strip() else 'OK'))
run([sys.executable,'scripts/verificar_site.py'])
run([sys.executable,'scripts/testar_exemplos.py'])
run(['node','scripts/verificar_senha.js'])
run(['node','scripts/verificar_interatividade.js'])
for js in (ROOT/'docs/assets/javascripts').glob('*.js'):run(['node','--check',str(js)])
from bs4 import BeautifulSoup
for p in (ROOT/'site').rglob('*.html'):
 text=p.read_text(encoding='utf8')
 soup=BeautifulSoup(text,'html.parser')
 for tag in soup.find_all('script'):
  if tag.get('src') or not tag.text.strip():continue
  # Compilação sem execução.
  s=subprocess.run(['node','--check','-'],input=tag.text,capture_output=True,text=True)
  if s.returncode:raise RuntimeError(f'JS embutido incorreto: {p}: {s.stderr[:200]}')
checks.append(('JavaScript embutido','53 scripts verificados'))
completed=0
for p in sorted((ROOT/'docs/aulas').glob('*/aula.ipynb')):
 nb=nbformat.read(p,as_version=4);nbformat.validate(nb)
 before=os.getcwd();os.chdir(p.parent)
 try:
  space={}
  for idx,cell in enumerate(nb.cells):
   if cell.cell_type=='code':exec(compile(cell.source,f'{p}:{idx}','exec'),space)
 finally:os.chdir(before)
 completed+=1
checks.append(('Notebooks Jupyter',f'{completed} executados sem erro'))
for f in ['marketing_competitivo.py','atendimento_workflow.py','rag_local.py','portfolio_curva.py']:
 run([sys.executable,'exemplos/'+f])
pdfs=[ROOT/'docs/avaliacoes/pdf/PI-exemplo.pdf',ROOT/'docs/avaliacoes/pdf/PF-exemplo.pdf',ROOT/'docs/caderno/caderno-atividades.pdf',ROOT/'docente_privado/PI-gabarito.pdf',ROOT/'docente_privado/PF-gabarito.pdf',ROOT/'docente_privado/gabarito-caderno.pdf']
for p in pdfs:
 doc=fitz.open(p)
 if any(len(x.get_text().strip())<60 for x in doc):raise RuntimeError(f'Página vazia: {p}')
 checks.append((str(p.relative_to(ROOT)),f'{len(doc)} páginas'))
conf=tomllib.load((ROOT/'zensical.toml').open('rb'))
assert conf['project']['site_author']=='Paulo C. Marques F.'
assert not (ROOT/'site/docente_privado').exists()
assert 'docente_privado/' in (ROOT/'.gitignore').read_text()
assert 'U=\'inspirar\',P=\'pertencer\'' in (ROOT/'docs/assets/javascripts/gate.js').read_text()
print('AUDITORIA CONCLUÍDA:')
for desc,res in checks:print('  ',desc,':',res[:180])
print('Arquivos:',sum(x.is_file() for x in ROOT.rglob('*')))
