"""Retrieval local: TF-IDF, BM25 didático, documentos identificados e corte por seção.

A busca nunca é apresentada como geração por um LLM.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import math,re
from collections import Counter
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@dataclass(frozen=True)
class Chunk:
    doc_id:str
    section:str
    text:str

@dataclass(frozen=True)
class Hit:
    doc_id:str
    section:str
    text:str
    score:float

def load_corpus(folder):
    folder=Path(folder)
    paths=sorted(folder.rglob('*.md'))
    if not paths: raise FileNotFoundError(f'Nenhum documento .md em {folder}')
    return {p.stem:p.read_text(encoding='utf-8') for p in paths}

def chunk_headings(corpus,max_chars=1250):
    """Preserva títulos e seções; quebra parágrafos grandes sem misturar documentos."""
    chunks=[]
    for doc_id,text in corpus.items():
        section='Início'; part=[]
        def flush():
            if part:
                chunks.append(Chunk(doc_id,section,'\n'.join(part).strip()))
                part.clear()
        for line in text.splitlines():
            if line.startswith('#'):
                flush();section=line.lstrip('# ').strip()
            elif line.strip():
                if sum(len(x) for x in part)+len(line)>max_chars and part:flush()
                if len(line)>max_chars:
                    flush()
                    for i in range(0,len(line),max_chars):chunks.append(Chunk(doc_id,section,line[i:i+max_chars]))
                else:part.append(line)
        flush()
    return chunks

class TfidfIndex:
    def __init__(self,chunks):
        self.chunks=list(chunks)
        if not self.chunks:raise ValueError('índice vazio')
        self.vectorizer=TfidfVectorizer(ngram_range=(1,2),strip_accents='unicode',lowercase=True)
        self.matrix=self.vectorizer.fit_transform([f'{c.doc_id} {c.section} {c.text}' for c in self.chunks])
    def search(self,query,k=3):
        if k<1:raise ValueError('k deve ser positivo')
        scores=cosine_similarity(self.vectorizer.transform([query]),self.matrix).ravel()
        order=np.argsort(-scores,kind='stable')[:k]
        return [Hit(self.chunks[i].doc_id,self.chunks[i].section,self.chunks[i].text,float(scores[i])) for i in order]

class BM25Index:
    """Implementação local suficiente para atividades; idf suavizada, k1=1.5, b=.75."""
    def __init__(self,chunks,k1=1.5,b=0.75):
        self.chunks=list(chunks); self.k1=k1;self.b=b
        self.tokens=[self._tokenize(f'{c.doc_id} {c.section} {c.text}') for c in self.chunks]
        if not self.tokens:raise ValueError('índice vazio')
        self.freq=[Counter(t) for t in self.tokens];self.avgdl=sum(map(len,self.tokens))/len(self.tokens)
        self.df=Counter(word for tokens in self.tokens for word in set(tokens))
    @staticmethod
    def _tokenize(s):return re.findall(r'\w+',s.lower(),re.UNICODE)
    def search(self,query,k=3):
        n=len(self.chunks);query_tokens=self._tokenize(query);out=[]
        for i,tf in enumerate(self.freq):
            dl=len(self.tokens[i]);sc=0.0
            for w in query_tokens:
                if w not in tf:continue
                df=self.df[w];idf=math.log(1+(n-df+.5)/(df+.5));f=tf[w]
                sc+=idf*f*(self.k1+1)/(f+self.k1*(1-self.b+self.b*dl/self.avgdl))
            c=self.chunks[i];out.append(Hit(c.doc_id,c.section,c.text,float(sc)))
        return sorted(out,key=lambda h:-h.score)[:k]

# IMPORTANT: A separação dados x instruções precisa ser implementada na aplicação.
# Estes índices apenas recuperam texto. Eles NÃO aplicam políticas de acesso.
