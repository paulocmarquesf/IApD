"""Workflow determinístico de consulta local com trilha, sem ações externas."""
from __future__ import annotations
from dataclasses import dataclass,field
from pathlib import Path
from .finance import variacao_percentual
import pandas as pd

CAMPOS={'inflacao_mensal_pct','juros_anuais_pct','desemprego_pct','expectativa_12m_pct'}

@dataclass
class Resultado:
    resposta:str
    fonte:str|None
    etapas:list[str]=field(default_factory=list)
    precisa_aprovacao:bool=False

def consultar_serie(csv_path,campo,mes):
    if campo not in CAMPOS:raise ValueError('campo não permitido')
    df=pd.read_csv(csv_path)
    rows=df.loc[df['mes']==mes,campo]
    if len(rows)!=1:raise LookupError('período ausente ou duplicado')
    return float(rows.iloc[0])

def executar_consulta_macro(csv_path, pergunta, *, max_etapas=4):
    log=['classificar_intencao']
    if max_etapas<2:raise ValueError('limite de etapas insuficiente')
    if 'oficial' in pergunta.lower():
        log.append('verificar_escopo_da_fonte')
        return Resultado('O corpus contém somente dados simulados; nenhuma taxa oficial pode ser informada.',None,log)
    if 'infla' in pergunta.lower():campo='inflacao_mensal_pct'
    elif 'desemprego' in pergunta.lower():campo='desemprego_pct'
    else:return Resultado('Informe uma variável disponível e um período.',None,log+['solicitar_esclarecimento'])
    df=pd.read_csv(csv_path)
    log.append('consultar_serie')
    mes=df['mes'].iloc[-1];value=consultar_serie(csv_path,campo,mes)
    log.append('verificar_periodo_e_unidade')
    return Resultado(f'{campo} em {mes}: {value:.2f} (valor simulado; unidade do cabeçalho).',str(csv_path),log)

def autorizar_acao(acao,aprovacao_humana=False):
    """Política didática: apenas ações read-only e resumo fictício; aprovação não amplia escopo."""
    if acao in {'consultar_serie','calcular','buscar_documento','resumir'}:return True
    return False
