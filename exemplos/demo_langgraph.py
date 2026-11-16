"""LangGraph opcional. StateGraph read-only sem chamadas a LLM ou serviços externos."""
from typing import TypedDict
from langgraph.graph import StateGraph,START,END
class State(TypedDict):
    pergunta: str
    resultado: str
    fonte: str

def consultar(s:State)->dict:
    if 'oficial' in s['pergunta'].lower():
        return {'resultado':'Não há fonte oficial neste corpus didático.', 'fonte':'nenhuma'}
    return {'resultado':'Dados simulados: consultar arquivo macro_simulada.csv.', 'fonte':'macro_simulada.csv'}

def main():
    graph=StateGraph(State)
    graph.add_node('consultar',consultar)
    graph.add_edge(START,'consultar');graph.add_edge('consultar',END)
    agent=graph.compile()
    print(agent.invoke({'pergunta':'Qual a Selic oficial?', 'resultado':'', 'fonte':''}))
if __name__=='__main__':main()
