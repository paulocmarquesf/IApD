"""Testes dos contratos do material didático."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import pytest
from iad.finance import inflacao_acumulada,retorno_sobre_custo,margem_operacional,retorno_simples,verificar_comparabilidade
from iad.metrics import precisao_recall,recall_at_k,mean_reciprocal_rank
from iad.workflow import autorizar_acao,executar_consulta_macro
from iad.retrieval import load_corpus,chunk_headings,TfidfIndex,BM25Index
ROOT=Path(__file__).resolve().parents[1]

def test_basicos_financas():
 assert retorno_sobre_custo(12000,8000)==.5
 assert margem_operacional(165,1000)==.165
 assert abs(inflacao_acumulada([1,1])-2.01)<1e-8
 with pytest.raises(ValueError):retorno_sobre_custo(100,0)
 assert verificar_comparabilidade('T2','T2','BRL','BRL')
 assert not verificar_comparabilidade('T2','T1','BRL','BRL')

def test_indices_retrieval():
 corpus=load_corpus(ROOT/'dados/relatorios')
 chunks=chunk_headings(corpus,max_chars=800)
 assert len(chunks)>len(corpus)
 for cls in (TfidfIndex,BM25Index):
  res=cls(chunks).search('receita líquida 2026 segundo trimestre',k=3)
  assert len(res)==3
  assert all(hasattr(hit,'doc_id') for hit in res)

def test_metricas():
 p,r=precisao_recall(12,6,8)
 assert p==pytest.approx(2/3) and r==pytest.approx(.6)
 ranks=[['a','b'],['c','d'],['e']]
 gold=['a','d','x']
 assert recall_at_k(ranks,gold,1)==pytest.approx(1/3)
 assert recall_at_k(ranks,gold,2)==pytest.approx(2/3)
 assert mean_reciprocal_rank(ranks,gold)==pytest.approx(.5)
 assert recall_at_k([['a']],[None],1) is None

def test_agente_permissaos():
 for action in ('comprar_ativo','enviar_email','exportar_dados_pessoais'):
  assert not autorizar_acao(action,aprovacao_humana=True)
 for action in ('consultar_serie','buscar_documento','calcular'):
  assert autorizar_acao(action)
 r=executar_consulta_macro(ROOT/'dados/macro_simulada.csv','Qual a taxa Selic oficial de hoje?')
 assert r.fonte is None and 'oficial' in r.resposta

def test_documentos_rotulados_ficticios():
 for p in (ROOT/'dados/relatorios').glob('*.md'):
  assert 'FICTÍCIO' in p.read_text(encoding='utf8')
