#!/usr/bin/env python3
"""Compila notebooks locais e decks HTML independentes para as 12 aulas."""
from __future__ import annotations
from pathlib import Path
import sys, html, re, json, textwrap
import nbformat as nbf
sys.path.insert(0,str(Path(__file__).resolve().parent))
from construir_curso import LESSONS,ROOT,DOCS

HEADER='''from pathlib import Path
import sys
import numpy as np
import pandas as pd

# Localiza a raiz do curso, inclusive ao abrir o notebook a partir da pasta da aula.
def achar_raiz():
    origem = Path.cwd().resolve()
    for pasta in (origem, *origem.parents):
        if (pasta / "dados" / "README.md").exists() and (pasta / "src").exists():
            return pasta
    raise FileNotFoundError("Abra o notebook dentro do repositório extraído, preservando dados/ e src/.")

ROOT = achar_raiz()
sys.path.insert(0, str(ROOT / "src"))
print("Repositório:", ROOT)
'''

# Cada notebook executa cálculos locais concretos; toda chamada externa é opt-in.
CELLS={
1:[
('Tokens e probabilidades','''# Simulamos a escolha do próximo token a partir de escores fixos.
logits = np.array([3.7, 2.5, 1.8, 0.4])
tokens = ['cresceu','caiu','ficou','explodiu']
def softmax(z):
    e=np.exp(z-np.max(z))
    return e/e.sum()
for temperatura in [0.2,0.8,1.5]:
    probabilidades=softmax(logits/temperatura)
    print('T=',temperatura, dict(zip(tokens, np.round(probabilidades,3))))'''),
('Uma previsão precisa de dados','''vendas = pd.Series([100,110,90,120], name='vendas_mil_reais')
baseline = vendas.mean()
print('Baseline (R$ mil):', baseline)
print('Uma resposta sem dados de vendas é apenas uma hipótese textual; não é previsão validada.')'''),
('Refutação do palpite','''assert np.isclose(softmax(logits/0.8).sum(),1)
print('Qual informação faltaria para medir MAE de previsões semanais?')''')],
2:[
('Cosseno de vetores','''from sklearn.metrics.pairwise import cosine_similarity
vetores=np.array([[3,0],[6,0],[0,3]])
print('Matriz de cossenos:')
print(cosine_similarity(vetores))
print('Distância entre os dois primeiros:',np.linalg.norm(vetores[0]-vetores[1]))'''),
('Busca lexical em descrições','''from sklearn.feature_extraction.text import TfidfVectorizer
catalogo=pd.read_csv(ROOT/'dados/catalogo_produtos.csv')
vectorizer=TfidfVectorizer(strip_accents='unicode',ngram_range=(1,2))
X=vectorizer.fit_transform(catalogo['descricao'])
q=vectorizer.transform(['bolsa acolchoada para computador'])
score=cosine_similarity(q,X).ravel()
print(catalogo.assign(similaridade=score).nlargest(5,'similaridade')[['produto','similaridade']].to_string(index=False))'''),
('Redução dimensional com cautela','''from sklearn.decomposition import TruncatedSVD
modelo=TruncatedSVD(n_components=2,random_state=42)
Z=modelo.fit_transform(X)
print('Proporção de variância do SVD em 2 dimensões:', np.round(modelo.explained_variance_ratio_.sum(),3))
print('A projeção perde informações; não usar o gráfico para provar substituição de produtos.')''')],
3:[
('Ler o documento','''texto=(ROOT/'dados/relatorios/horizonte-2026-t2.md').read_text(encoding='utf-8')
print('\\n'.join(texto.splitlines()[:17]))'''),
('Esquema e validação','''from dataclasses import dataclass
@dataclass
class Extracao:
    empresa:str
    periodo:str
    receita_milhoes:float|None
    resultado_operacional_milhoes:float|None
    lucro_milhoes:float|None
    fonte:str

registro=Extracao('Horizonte Comércio S.A.','2026-T2',1000,165,107,'horizonte-2026-t2')
print(registro)
print('Tipos válidos?',isinstance(registro.receita_milhoes,(int,float)))'''),
('Verificação quantitativa independente','''from iad.finance import margem_operacional
m=margem_operacional(registro.resultado_operacional_milhoes,registro.receita_milhoes)
print('Margem operacional:',f'{m:.2%}')
assert abs(m-0.165)<1e-12
print('Agora troque a receita no registro: o tipo continua válido, mas a fonte deixa de conferir.')''')],
4:[
('Base e classe majoritária','''df=pd.read_csv(ROOT/'dados/avaliacoes_rotuladas.csv')
print(df['categoria'].value_counts().head(9).to_string())
print('Taxa de encaminhamento humano:',df['encaminhar_humano'].mean())'''),
('Matriz de confusão','''from iad.metrics import classification_report_counts
r=classification_report_counts(tp=12,fp=6,fn=8,tn=74)
print({k:round(v,3) for k,v in r.items()})
assert abs(r['precisao']-12/18)<1e-12'''),
('Classificador básico com teste honesto','''from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
Xtr,Xte,ytr,yte=train_test_split(df['texto'],df['encaminhar_humano'],test_size=.3,random_state=42,stratify=df['encaminhar_humano'])
clf=make_pipeline(TfidfVectorizer(strip_accents='unicode'),LogisticRegression(max_iter=300))
clf.fit(Xtr,ytr)
print(classification_report(yte,clf.predict(Xte),zero_division=0))
print('ATENÇÃO: base sintética com textos repetidos entre treino e teste; NÃO é estimativa de produção.')''')],
5:[
('Contratos de ferramenta','''from iad.finance import retorno_sobre_custo,margem_operacional
print('Retorno sobre custo:',f'{retorno_sobre_custo(12000,8000):.0%}')
print('Margem operacional:',f'{margem_operacional(165,1000):.1%}')'''),
('Base com atribuição','''df=pd.read_csv(ROOT/'dados/campanhas_simuladas.csv')
df['indicador']=(df['receita_atribuida_brl']-df['custo_brl'])/df['custo_brl']
print(df[['campanha','canal','indicador']].head(7).to_string(index=False))'''),
('Tratamento de erro','''try:
    retorno_sobre_custo(1000,0)
except ValueError as exc:
    print('A ferramenta recusou a conta:',exc)
print('Receita atribuída não permite calcular ganho causal incremental.')''')],
6:[
('Retornos mensais e dispersão','''from iad.finance import inflacao_acumulada
cotas=pd.read_csv(ROOT/'dados/cotas_fundos_simulados.csv')
retornos=cotas[['fundo_alpha','fundo_beta','renda_curta']].pct_change().dropna()
print('Médias mensais (%):\\n',(100*retornos.mean()).round(2))
print('Desvios mensais (%):\\n',(100*retornos.std()).round(2))'''),
('Diferença entre soma e composição','''print('Dois meses de 1% =',inflacao_acumulada([1,1]),'%')
macro=pd.read_csv(ROOT/'dados/macro_simulada.csv')
print('Inflação mensal simulada (primeiros quatro meses):',macro['inflacao_mensal_pct'].head().tolist())'''),
('Interpretação e limites','''print('Período coberto:',cotas.mes.iloc[0],'até',cotas.mes.iloc[-1])
print('Variações de cota passadas NÃO constituem recomendação de investimento.')''')],
7:[
('Corpus e cortes por título','''from iad.retrieval import load_corpus,chunk_headings,TfidfIndex,BM25Index
corpus=load_corpus(ROOT/'dados/relatorios')
corpus.update(load_corpus(ROOT/'dados/faq'))
chunks=chunk_headings(corpus,max_chars=900)
print('Documentos:',len(corpus),'Trechos:',len(chunks))
print(chunks[0])'''),
('Recuperação TF-IDF e BM25','''tf=TfidfIndex(chunks)
bm=BM25Index(chunks)
pergunta='receita líquida da Horizonte no segundo trimestre de 2026'
for name,index in [('TF-IDF',tf),('BM25',bm)]:
    print(name,[(h.doc_id,h.section,round(h.score,3)) for h in index.search(pergunta,k=3)])'''),
('Regra de citação','''fontes={h.doc_id for h in tf.search(pergunta,k=3)}
print('Documentos recuperados:',fontes)
print('Um trecho não encontrado não autoriza o sistema a inventar um número.')''')],
8:[
('Perguntas e documentos esperados','''from iad.retrieval import load_corpus,chunk_headings,TfidfIndex
base=load_corpus(ROOT/'dados/relatorios')
base.update(load_corpus(ROOT/'dados/faq'))
base.update(load_corpus(ROOT/'dados/comunicados'))
indice=TfidfIndex(chunk_headings(base,max_chars=1250))
perguntas=pd.read_csv(ROOT/'dados/perguntas_rag.csv')
print(perguntas.to_string(index=False))'''),
('Resposta com período e evidência','''q='Qual foi a receita da Horizonte no segundo trimestre de 2026?'
for h in indice.search(q,k=3):
    print(h.doc_id, '|',h.section,'| score',round(h.score,3))
print('Conferência manual da fonte: horizonte-2026-t2 → receita 1000 (R$ milhões).')'''),
('Abster-se é necessário','''ausente='Qual foi a Selic oficial de junho de 2026?'
print('Pergunta:',ausente)
print('Resposta segura: não consta informação oficial neste corpus sintético.')''')],
9:[
('Avaliar retrieval, não geração','''from iad.metrics import recall_at_k, mean_reciprocal_rank
from iad.retrieval import load_corpus,chunk_headings,TfidfIndex
base=load_corpus(ROOT/'dados/relatorios');base.update(load_corpus(ROOT/'dados/faq'));base.update(load_corpus(ROOT/'dados/comunicados'))
idx=TfidfIndex(chunk_headings(base,max_chars=1250))
questoes=pd.read_csv(ROOT/'dados/perguntas_rag.csv')
rankings=[[h.doc_id for h in idx.search(q,k=20)] for q in questoes.pergunta]
gold=[None if x=='nenhuma' else x for x in questoes.documento_esperado]
print('Recall@1:',recall_at_k(rankings,gold,1))
print('Recall@3:',recall_at_k(rankings,gold,3))
print('MRR:',mean_reciprocal_rank(rankings,gold))'''),
('Diagnóstico por caso','''for i,row in questoes.iterrows():
    print('Q',i+1, 'gabarito:',row.documento_esperado, 'top2:',rankings[i][:2])
print('Para questões sem fonte, a avaliação da resposta exige verificar abstenção.')''')],
10:[
('Ablar o tamanho de chunks','''from iad.retrieval import load_corpus,chunk_headings,TfidfIndex
from iad.metrics import recall_at_k
base=load_corpus(ROOT/'dados/relatorios');base.update(load_corpus(ROOT/'dados/faq'));base.update(load_corpus(ROOT/'dados/comunicados'))
q=pd.read_csv(ROOT/'dados/perguntas_rag.csv')
gold=[None if x=='nenhuma' else x for x in q.documento_esperado]
for max_chars in [250,650,1300]:
    chunks=chunk_headings(base,max_chars=max_chars)
    idx=TfidfIndex(chunks)
    ranks=[[h.doc_id for h in idx.search(texto,k=5)] for texto in q.pergunta]
    print(max_chars,'chars, chunks:',len(chunks),'Recall@2:',round(recall_at_k(ranks,gold,2),3))'''),
('Mudar k no mesmo experimento','''idx=TfidfIndex(chunk_headings(base,max_chars=650))
ranks=[[h.doc_id for h in idx.search(texto,k=10)] for texto in q.pergunta]
print({k:recall_at_k(ranks,gold,k) for k in [1,2,3,5]})
print('Recall retrieval não equivale a fidelidade de geração.')''')],
11:[
('Workflow read-only','''from iad.workflow import executar_consulta_macro
arquivo=ROOT/'dados/macro_simulada.csv'
for pergunta in ['Resuma inflação simulada','Qual foi o desemprego simulado?','Informe a Selic oficial agora']:
    resultado=executar_consulta_macro(arquivo,pergunta)
    print('\\nPERGUNTA:',pergunta)
    print('TRAJETO:',resultado.etapas)
    print('RESPOSTA:',resultado.resposta)'''),
('Política e limite de ações','''from iad.workflow import autorizar_acao
for acao in ['consultar_serie','calcular','buscar_documento','enviar_email','comprar_ativo']:
    print(acao,autorizar_acao(acao,aprovacao_humana=True))
print('Aprovação humana não amplia o conjunto de ações permitidas.')''')],
12:[
('Casos normais e adversariais','''msgs=pd.read_csv(ROOT/'dados/avaliacoes_rotuladas.csv')
atq=msgs[msgs.texto.str.contains('ignore|Atue como administrador',case=False,regex=True)]
print('Entradas que contêm tentativas de instrução:')
print(atq[['id','texto','categoria']].to_string(index=False))'''),
('Separar política de documento','''from iad.workflow import autorizar_acao
requisicoes=['resumir','buscar_documento','comprar_ativo','exportar_dados_pessoais']
print({x:autorizar_acao(x) for x in requisicoes})
print('Ações fora da lista autorizada permanecem proibidas, mesmo que um PDF peça.')'''),
('Trilha de auditoria','''trilha=[{'passo':1,'acao':'buscar_documento','resultado':'fonte fictícia'},
       {'passo':2,'acao':'validar_unidades','resultado':'ok'},
       {'passo':3,'acao':'publicar_dados','resultado':'bloqueado'}]
print(pd.DataFrame(trilha).to_string(index=False))''')]
}

for L in LESSONS:
    n=L['n']; out=DOCS/'aulas'/L['slug']/'aula.ipynb'
    nb=nbf.v4.new_notebook()
    nb.metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python'}}
    cells=[nbf.v4.new_markdown_cell(f'''# Aula {n:02d} | {L['title']}

**Inteligência Artificial para Decisão** · {L['domain']} · notebook local.

**Pergunta:** {L['q']}

**Procedimento:** execute as células, confira os resultados e modifique uma hipótese. Não há chamadas a serviços externos. Todos os dados são sintéticos ou fictícios.
'''),nbf.v4.new_code_cell(HEADER)]
    for title,code in CELLS[n]:
        cells += [nbf.v4.new_markdown_cell(f'## {title}'), nbf.v4.new_code_cell(code)]
    cells += [nbf.v4.new_markdown_cell(f'''## Síntese individual

1. Qual pergunta este experimento responde e qual **não** responde?
2. Que valores foram calculados e quais foram apenas interpretados?
3. Que alteração você realizou? Registre a saída e explique sua escolha.
4. Qual erro seria especialmente relevante para uma decisão em **{L['domain']}**?

**Entrega:** {L['artifact']}''')]
    nb.cells=cells
    nbf.validate(nb)
    nbf.write(nb,out)

# Deck HTML: 9 slides cuidadosamente curados por aula.
SPECIAL={
 1:['O texto provável não é uma previsão validada','Prever vendas requer dados e um erro fora da amostra','P(t₁,…,tₘ | c) = ∏ P(tⱼ | c,t<ⱼ)','Temperatura muda a seleção, não a base factual','Baseline: média de 100,110,90,120 = 105 mil','A pergunta decisiva: que informação faltou?'],
 2:['Concorrência é uma relação definida pelo problema','Vetores tornam descrições comparáveis','sim(u,v) = u·v / (‖u‖‖v‖)','Lexical: coincidência de palavras; semântica: sentido','Cosseno 1 não significa substituição econômica','Projete para visualizar, mas não confunda mapa e mercado'],
 3:['Extrair números não é interpretá-los','Contrato: campos, tipos, unidades, nulos','JSON válido ≠ fato verificado','Horizonte T2: 1000 de receita, 165 operacional','Margem operacional: 165/1000 = 16,5%','A fonte documental decide, não o formato'],
 4:['Acurácia pode esconder a classe de interesse','Classificação é decisão sob erros assimétricos','Precisão = VP/(VP+FP)','Recall = VP/(VP+FN)','Uma reclamação pode conter prompt injection','O teste deve preceder a decisão de implantação'],
 5:['Tool calling é uma arquitetura, não uma conta mágica','O modelo escolhe; a função calcula','Parâmetros devem ter mesma unidade e período','(12000−8000)/8000 = 50%','Receita atribuída ≠ incremento causal','Uma ferramenta também deve falhar com clareza'],
 6:['Uma aplicação composta pode ser determinística','Retorno simples = P(t)/P(t−1) − 1','Volatilidade histórica depende da janela','Dois meses de 1% → 2,01% acumulados','Cotas e indicadores fornecidos são simulados','Explicar o cálculo não implica recomendar um ativo'],
 7:['RAG é recuperar antes de gerar','Documentos → chunks → índice → trechos → resposta','Cada trecho leva ID, seção e período','TF-IDF e BM25 competem com embeddings','Fonte recuperada não garante resposta correta','Sem evidência, a abstenção é legítima'],
 8:['Relatórios e comunicados exigem leituras distintas','Duas fontes para comparar dois trimestres','T1: 15,76%; T2: 16,50%','Variação: +0,74 ponto percentual','Comunicados fictícios não são atas do Copom','A fonte e a cronologia devem acompanhar o resultado'],
 9:['Avaliar separadamente buscar e responder','Recall@k mede cobertura de fonte','MRR incorpora a posição do primeiro acerto','Citação correta pode sustentar número errado','Abstenção correta é um resultado positivo','Sem conjunto de teste, melhora é impressão'],
10:['Melhorar exige experimento controlado','Variar chunks, k, híbrido e reranking','Mais fontes podem introduzir ruído','Com mesmo teste, compare cobertura e custos','Ajuste no desenvolvimento; avalie no teste','Diagnostique antes de aumentar a complexidade'],
11:['Um workflow não precisa de autonomia','Agente escolhe ação dentre permissões explícitas','Estado e transições são verificáveis','LangGraph é uma implementação possível','Timeout, limite de passos e erros são essenciais','Sem fonte oficial, o agente deve encerrar e explicar'],
12:['Avaliar o resultado e a trajetória','Documento externo é dado, não instrução','Permissões mínimas limitam danos','Aprovação não é autorização irrestrita','Teste casos normais, falhas e ataques','Confiabilidade exige supervisão e mecanismos de parada'],
}

def esc(s):return html.escape(s,quote=True)

def slide(sec,i,n):
    kind,head,body=sec
    body_html=body if kind=='html' else f'<p class="statement">{esc(body)}</p>'
    return f'<section class="slide" data-index="{i}"><div class="eyebrow">AULA {n:02d} / INTELIGÊNCIA ARTIFICIAL PARA DECISÃO</div><div class="slide-main"><div class="serial">{i+1:02d} <span>—</span> 09</div><h1>{esc(head)}</h1>{body_html}</div><div class="bottom"><span>ECONOMIA · ADMINISTRAÇÃO</span><span>CONCEITO &nbsp; / &nbsp; EXPERIMENTO &nbsp; / &nbsp; DECISÃO</span></div></section>'

for L in LESSONS:
    n=L['n'];src=SPECIAL[n]
    concept='<div class="concept-grid">'+''.join(f'<div><span>{j+1:02d}</span><p>{esc(c)}</p></div>' for j,c in enumerate(L['concepts']))+'</div>'
    sections=[('text',L['title'],L['q']),('text','O problema',L['case']),('html','Quatro conceitos',concept),
              ('text','Ideia 1',src[0]),('text','Ideia 2',src[1]),('text','Ideia 3',src[2]),('text','Exemplo e cuidado',src[3]+'\n'+src[4]),
              ('text','Uma limitação decisiva',src[5]),('text','O que deve permanecer',L['artifact'])]
    html_slides='\n'.join(slide(s,i,n) for i,s in enumerate(sections))
    dest=DOCS/'aulas'/L['slug']/'slides'/'aula.html';dest.parent.mkdir(exist_ok=True)
    dest.write_text(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Aula {n:02d} — {esc(L['title'])}</title><style>
:root{{--navy:#122840;--gold:#c9a36a;--muted:#97aabd}}*{{box-sizing:border-box}}body{{margin:0;background:#0b1928;color:#eff5f8;font-family:system-ui,-apple-system,Segoe UI,sans-serif}}.deck{{position:relative;width:100%;height:100vh;overflow:hidden}}.slide{{display:none;position:absolute;inset:0;padding:5vh 6vw 4vh;background:radial-gradient(ellipse at 84% 9%,#2b4960 0,#14293f 49%,#0e2236 100%);overflow:auto}}.slide.active{{display:flex;flex-direction:column}}.slide:after{{content:'';position:absolute;right:4vw;top:11vh;width:26vw;height:26vw;border:1px solid rgba(202,163,106,.14);border-radius:100%;pointer-events:none}}.eyebrow{{font-size:clamp(9px,1.05vw,15px);letter-spacing:.17em;color:var(--gold);font-weight:750}}.slide-main{{margin:auto 0;max-width:1020px;z-index:1}}.serial{{color:var(--gold);letter-spacing:.09em;font-size:clamp(13px,1.5vw,21px);margin-bottom:2.8vh}}.serial span{{color:#718499;margin:0 12px}}h1{{font-family:Georgia,serif;font-weight:400;line-height:1.13;letter-spacing:-.045em;font-size:clamp(27px,5.0vw,82px);max-width:1050px;margin:0 0 4vh}}.statement{{font-size:clamp(16px,2vw,28px);line-height:1.55;white-space:pre-line;color:#b9c9d6;max-width:950px}}.bottom{{display:flex;justify-content:space-between;border-top:1px solid #43576b;padding-top:16px;font-size:clamp(9px,.9vw,13px);letter-spacing:.11em;color:#9eafbd}}.controls{{position:fixed;bottom:24px;right:25px;display:flex;gap:7px;z-index:10}}button{{background:#c8a26a;border:0;color:#10263b;padding:10px 16px;border-radius:4px;font-weight:700;cursor:pointer}}button:hover{{background:#e2be85}}.count{{position:fixed;bottom:36px;left:20px;z-index:10;font-size:12px;color:#94a8b9}}.concept-grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;max-width:860px}}.concept-grid div{{border:1px solid #62758a;padding:1rem 1.4rem;border-radius:7px;background:rgba(0,0,0,.08)}}.concept-grid span{{color:var(--gold);font-family:Georgia,serif;font-size:24px}}.concept-grid p{{font-size:clamp(14px,1.5vw,20px);line-height:1.45}}.overview .deck{{height:auto;overflow:visible;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:12px}}.overview .slide{{display:flex;position:relative;min-height:28vh;inset:auto;padding:20px;overflow:hidden;border:1px solid #45607d;cursor:pointer}}.overview .slide h1{{font-size:clamp(16px,1.5vw,26px)}}.overview .slide .statement{{display:none}}.overview .slide .serial{{margin:0 0 15px}}.overview .slide .eyebrow,.overview .slide .bottom{{display:none}}.overview .concept-grid{{display:none}}@media(max-width:680px){{.slide{{padding:4vh 7vw 7vh}}.concept-grid{{grid-template-columns:1fr}}.bottom span:last-child{{display:none}}.overview .deck{{grid-template-columns:1fr 1fr}}}}
</style></head><body><div class="deck">{html_slides}</div><div class="count" id="counter">1 / 9</div><div class="controls"><button type="button" id="prev" aria-label="Anterior">←</button><button type="button" id="next" aria-label="Próximo">→</button><button type="button" id="overview" aria-label="Visão geral">▦</button><button type="button" id="full" aria-label="Tela cheia">⛶</button></div><script>
let current=0;const slides=[...document.querySelectorAll('.slide')];function show(i){{current=Math.max(0,Math.min(slides.length-1,i));slides.forEach((s,j)=>s.classList.toggle('active',j===current));document.querySelector('#counter').textContent=(current+1)+' / '+slides.length;}}function toggleOverview(){{document.body.classList.toggle('overview');}}document.querySelector('#next').onclick=()=>show(current+1);document.querySelector('#prev').onclick=()=>show(current-1);document.querySelector('#overview').onclick=toggleOverview;document.querySelector('#full').onclick=()=>document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen?.();document.addEventListener('keydown',e=>{{if(['ArrowRight','PageDown',' '].includes(e.key)){{e.preventDefault();show(current+1)}}if(['ArrowLeft','PageUp'].includes(e.key)){{e.preventDefault();show(current-1)}}if(e.key==='Escape'){{document.body.classList.remove('overview')}}if(e.key.toLowerCase()==='f')document.documentElement.requestFullscreen?.();}});slides.forEach((s,i)=>s.addEventListener('click',()=>{{if(document.body.classList.contains('overview')){{document.body.classList.remove('overview');show(i)}}}}));show(0);
</script></body></html>''',encoding='utf-8')

print('GERADOR: criados',len(LESSONS),'notebooks e decks com 9 slides cada')
