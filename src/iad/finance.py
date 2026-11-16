"""Cálculos locais. Receitas atribuídas não equivalem a efeitos causais."""
from __future__ import annotations
import numpy as np
import pandas as pd

def retorno_sobre_custo(receita_atribuida: float, custo: float) -> float:
    if custo <= 0: raise ValueError('custo deve ser positivo')
    return (receita_atribuida-custo)/custo

def margem_operacional(resultado_operacional: float, receita_liquida: float) -> float:
    if receita_liquida <= 0: raise ValueError('receita deve ser positiva')
    return resultado_operacional/receita_liquida

def variacao_percentual(atual: float, anterior: float) -> float:
    if anterior == 0: raise ValueError('denominador zero')
    return (atual-anterior)/abs(anterior)

def retorno_simples(cotas):
    s=pd.Series(cotas,dtype='float64')
    if (s <= 0).any(): raise ValueError('cotas precisam ser positivas')
    return s.pct_change().dropna()

def inflacao_acumulada(taxas_percentuais) -> float:
    """Retorna percentual acumulado, se a entrada for em percentuais (1=1%)."""
    taxas=np.asarray(list(taxas_percentuais),dtype=float)
    if np.any(taxas <= -100): raise ValueError('taxa precisa ser maior que -100%')
    return float(100*(np.prod(1+taxas/100)-1))

def verificar_comparabilidade(periodo_a,periodo_b,unidade_a,unidade_b):
    return periodo_a==periodo_b and unidade_a==unidade_b
