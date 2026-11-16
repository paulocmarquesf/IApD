"""Métricas definidas explicitamente para evitar confusões de denominadores."""
from __future__ import annotations

def precisao_recall(tp:int,fp:int,fn:int):
    if min(tp,fp,fn)<0: raise ValueError('contagens não podem ser negativas')
    return (tp/(tp+fp) if tp+fp else None, tp/(tp+fn) if tp+fn else None)

def recall_at_k(rankings, references, k:int):
    """Uma fonte relevante por pergunta; as consultas com fonte ausente são excluídas.

    `rankings` é lista de listas de IDs de documentos;
    `references` é lista de IDs relevantes ou None para questões sem fonte.
    """
    if k < 1: raise ValueError('k precisa ser >=1')
    pairs=[(r,g) for r,g in zip(rankings,references) if g is not None]
    if not pairs:return None
    return sum(g in r[:k] for r,g in pairs)/len(pairs)

def mean_reciprocal_rank(rankings,references):
    pairs=[(r,g) for r,g in zip(rankings,references) if g is not None]
    if not pairs:return None
    score=0.0
    for ranking,gold in pairs:
        if gold in ranking:score+=1/(ranking.index(gold)+1)
    return score/len(pairs)

def classification_report_counts(tp,fp,fn,tn):
    p,r=precisao_recall(tp,fp,fn)
    total=tp+fp+fn+tn
    return {'precisao':p,'recall':r,'acuracia':(tp+tn)/total if total else None}
