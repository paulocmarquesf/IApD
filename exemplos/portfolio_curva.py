"""Carteiras em dados sintéticos. Demonstração; não é recomendação de investimento."""
from pathlib import Path
import csv,math,random,statistics,json
DATA=Path(__file__).resolve().parents[1]/'dados'

def returns_by_ticker():
    prices={}
    with (DATA/'prices_simulated.csv').open(encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):prices.setdefault(row['ticker'],[]).append(float(row['close']))
    return {tick:[y/x-1 for x,y in zip(v[:-1],v[1:])] for tick,v in prices.items()}

def analyze(seed=42,trials=8000):
    r=returns_by_ticker();tickers=sorted(r)
    if len({len(v) for v in r.values()})!=1:raise ValueError('Séries com datas desalinhadas')
    means=[statistics.mean(r[t]) for t in tickers]
    cov=[[statistics.covariance(r[x],r[y]) for y in tickers] for x in tickers]
    rng=random.Random(seed);best=None;frontier=[]
    for i in range(trials):
        w=[rng.random() for _ in tickers];tot=sum(w);w=[x/tot for x in w]
        mu=sum(w[j]*means[j] for j in range(len(w)))
        var=sum(w[j]*cov[j][k]*w[k] for j in range(len(w)) for k in range(len(w)))
        risk=math.sqrt(max(var,0));sharpe=(mu*252-.02)/(risk*math.sqrt(252)) if risk else -float('inf')
        if best is None or sharpe>best['sharpe']:
            best={'weights':dict(zip(tickers,w)),'return_annualized':mu*252,'volatility_annualized':risk*math.sqrt(252),'sharpe':sharpe}
        if i%500==0:frontier.append({'return_annualized':mu*252,'volatility_annualized':risk*math.sqrt(252)})
    return {'source':'synthetic_classroom','tickers':tickers,'best_of_sampled_portfolios':best,'frontier_sample':frontier}

if __name__=='__main__':print(json.dumps(analyze(),ensure_ascii=False,indent=2))
