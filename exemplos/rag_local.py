"""Recuperação lexical local em documentos fictícios, sem LLM ou API."""
from pathlib import Path
import re,math,collections,json
DATA=Path(__file__).resolve().parents[1]/'dados'

def tokens(text):return re.findall(r'\w+',text.casefold())

def documents():return {p.stem:p.read_text(encoding='utf-8') for p in (DATA/'fundos').glob('*.md')}

def search(query,k=2):
    docs=documents(); terms=set(tokens(query))
    def score(text):
        counts=collections.Counter(tokens(text))
        return sum(1+math.log(1+counts[t]) for t in terms if counts[t])
    ranked=sorted(((name,round(score(text),4)) for name,text in docs.items()),key=lambda x:x[1],reverse=True)
    return ranked[:k]

def rewrite(followup,previous):
    if 'Delta' in followup and 'taxa de administração' in previous:
        return 'Qual a taxa de administração do Fundo Delta?'
    return followup

if __name__=='__main__':
    query=rewrite('E a do Delta?','Qual a taxa de administração do Fundo Horizonte?')
    print(json.dumps({'rewritten_query':query,'documents':search(query)},ensure_ascii=False,indent=2))
