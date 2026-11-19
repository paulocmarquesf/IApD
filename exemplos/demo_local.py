"""Exemplos completamente locais, sem dependências nem credenciais."""
import math

def portfolio(w, mu_a=.08,mu_b=.12,sd_a=.10,sd_b=.20,correlation=0.0,risk_free=.02):
    if not 0<=w<=1: raise ValueError("Peso fora de 0..1")
    mu=w*mu_a+(1-w)*mu_b
    var=w*w*sd_a*sd_a+(1-w)**2*sd_b*sd_b+2*w*(1-w)*sd_a*sd_b*correlation
    sd=math.sqrt(var)
    return {"return":mu,"volatility":sd,"sharpe":(mu-risk_free)/sd if sd>0 else None}

def retrieval(ranks,k):
    if not ranks or k<1:raise ValueError("Informe ranking e k>0")
    return {"hit_at_k":sum(r<=k for r in ranks)/len(ranks),"mrr_at_k":sum((1/r if r<=k else 0) for r in ranks)/len(ranks)}

if __name__=="__main__":
    print("Carteira:",portfolio(.5))
    print("Busca A:",retrieval([1,3,2,5],3))
