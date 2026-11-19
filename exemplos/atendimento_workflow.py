"""Simulação de processo, sem ações externas e sem dados pessoais."""
from pathlib import Path
import csv,json
DATA=Path(__file__).resolve().parents[1]/'dados'

def lookup_order(order_id):
    with (DATA/'orders.csv').open(encoding='utf-8-sig') as f:
        for order in csv.DictReader(f):
            if order['order_id']==order_id:return order
    return None

def request_refund(order_id, approved=False):
    trace=[{'action':'lookup_order','input':order_id}]
    order=lookup_order(order_id)
    if order is None:
        trace.append({'action':'request_information'});return {'status':'missing_order','trace':trace}
    if order['status']!='delivered':
        trace.append({'action':'human_review','reason':'not_delivered'});return {'status':'human_review','trace':trace}
    days=int(order['days_since_delivery'])
    trace.append({'action':'check_policy','days':days})
    if days>7:
        trace.append({'action':'human_review','reason':'outside_window'});return {'status':'human_review','trace':trace}
    trace.append({'action':'eligibility_review'})
    if not approved:
        trace.append({'action':'request_approval'});return {'status':'awaiting_approval','trace':trace}
    trace.append({'action':'simulate_refund','note':'no payment sent'})
    return {'status':'simulated_only','trace':trace}

if __name__=='__main__':
    for oid in ['P0001','P0009','P9999']:
        print(oid,json.dumps(request_refund(oid,approved=False),ensure_ascii=False))
