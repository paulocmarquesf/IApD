"""Demonstração local de composição de ferramentas, sem serviços externos."""
from pathlib import Path
import csv,math,json
DATA=Path(__file__).resolve().parents[1]/'dados'

def get_brands():
    with (DATA/'brands_market.csv').open(encoding='utf-8-sig') as f:
        return {r['brand']:r for r in csv.DictReader(f)}

def closest_competitor(brand, rows):
    if brand not in rows:raise KeyError(brand)
    x=rows[brand]
    def distance(other):
        return math.sqrt(sum((float(x[a])-float(other[a]))**2 for a in ('quality_score','price_score','convenience_score')))
    return min(((k,distance(v)) for k,v in rows.items() if k!=brand), key=lambda pair:pair[1])

def market_share_change(brand,rows):
    row=rows[brand];a=float(row['share_2025']);b=float(row['share_2026'])
    return {'pp':b-a,'relative':(b-a)/a}

def analyze(brand):
    log=[]
    rows=get_brands();log.append({'tool':'get_brands','result':'loaded'})
    other,dist=closest_competitor(brand,rows);log.append({'tool':'closest_competitor','input':brand,'result':other,'distance':dist})
    change=market_share_change(other,rows);log.append({'tool':'market_share_change','input':other,'result':change})
    return {'brand':brand,'closest_competitor':other,'change':change,'trace':log}

if __name__=='__main__':print(json.dumps(analyze('Atlas'),ensure_ascii=False,indent=2))
