from pathlib import Path
import sys,math
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"exemplos"))
from demo_local import portfolio,retrieval
p=portfolio(.5)
assert abs(p["return"]-.10)<1e-12
assert abs(p["volatility"]-math.sqrt(.0125))<1e-12
r=retrieval([1,3,2,5],3)
assert abs(r["hit_at_k"]-.75)<1e-12
assert abs(r["mrr_at_k"]-((1+1/3+1/2)/4))<1e-12
print("Exemplos locais: OK")
