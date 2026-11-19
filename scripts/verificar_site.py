from pathlib import Path
from html.parser import HTMLParser
import json,sys,tomllib,re,math,subprocess
root=Path(__file__).resolve().parents[1];docs=root/'docs';site=root/'site';errors=[];count=0

def check(condition,msg):
    global count
    count+=1
    if not condition:errors.append(msg)

conf=tomllib.loads((root/'zensical.toml').read_text(encoding='utf8'))
check(conf['project']['site_author']=='Paulo C. Marques F.','Nome do docente incorreto')
check((site/'index.html').exists(),'Prévia principal ausente')
check((docs/'assets'/'javascripts'/'gate.js').exists(),'Bloqueio JS ausente')
gate=(docs/'assets'/'javascripts'/'gate.js').read_text(encoding='utf8')
check("U='inspirar',P='pertencer'" in gate,'Credenciais JS incorretas')
class Parser(HTMLParser):
    def __init__(self):super().__init__();self.urls=[]
    def handle_starttag(self,tag,attrs):
        data=dict(attrs)
        if tag in {'a','img','script','link','iframe'}:
            x=data.get('href') or data.get('src')
            if x:self.urls.append(x)
for n in range(1,13):
    paths=list((docs/'aulas').glob(f'{n:02d}-*'))
    check(len(paths)==1,f'Aula {n:02d} não é única');
    if not paths:continue
    d=paths[0]
    for x in ['index.md','handout.md','aula.ipynb','slides/aula.html']:
        check((d/x).exists(),f'Aula {n:02d} sem {x}')
    check((docs/'assets'/'simuladores'/f'{n:02d}.html').exists(),f'Simulador {n:02d}')
    check((docs/'assets'/'diagramas'/f'{n:02d}.svg').exists(),f'Diagrama {n:02d}')
    check((docs/'assets'/'quizzes'/f'{n:02d}-conceitos.json').exists(),f'Quiz conceitual {n:02d}')
    if n<12:check((docs/'assets'/'quizzes'/f'{n:02d}-casa.json').exists(),f'Quiz domiciliar {n:02d}')
    content=(d/'index.md').read_text(encoding='utf8')
    for word in ['Codex','Atividade domiciliar','Exemplo mínimo','Laboratório','API','CLI']:
        check(word in content,f'Aula {n:02d} sem {word}')
    if n>1:check(f'{n-1:02d}-casa.json' in content,f'Aula {n:02d} não retoma quiz da anterior')
    check((site/'aulas'/d.name/'index.html').exists(),f'Aula {n:02d} ausente na prévia')
for q in (docs/'assets'/'quizzes').glob('*.json'):
    obj=json.loads(q.read_text(encoding='utf8'))
    for item in obj['questions']:
        check(len(item['options'])==4 and 0<=item['answer']<4,f'Questão inválida em {q}')
for x in ['PI','PF']:
    check((docs/'avaliacoes'/'pdf'/f'{x}-exemplo.pdf').exists(),f'Prova {x}')
    check((root/'docente_privado'/f'{x}-gabarito.pdf').exists(),f'Gabarito {x}')
check((docs/'caderno'/'caderno-atividades.pdf').exists(),'Caderno PDF ausente')
for doc in site.rglob('*.html'):
    parser=Parser();parser.feed(doc.read_text(encoding='utf8'))
    for url in parser.urls:
        if url.startswith(('http:','https:','mailto:','#','data:','javascript:')):continue
        path=url.split('#')[0].split('?')[0]
        if not path:continue
        target=(doc.parent/path).resolve()
        if target.is_dir(): target/= 'index.html'
        check(target.exists(),f'Link quebrado em {doc.relative_to(site)}: {url}')
from PIL import Image
img=Image.open(docs/'assets'/'images'/'insper-logo.png')
check(img.width>100 and img.height>20,'Logo inválido')
check(not (site/'docente_privado').exists(),'Material privado no site')
check('docente_privado/' in (root/'.gitignore').read_text(),'Gabarito não ignorado pelo git')
print(f'Verificações concluídas: {count} | falhas: {len(errors)}')
if errors:
    print('\n'.join(errors[:70]))
    sys.exit(1)
print('Estrutura, links locais, quizzes, senha e arquivos: OK')
