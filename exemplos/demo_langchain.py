"""Exemplo OPCIONAL: exige langchain-openai e OPENAI_API_KEY; custo de API possível."""
from __future__ import annotations
import os

def main():
    if not os.environ.get('OPENAI_API_KEY'):
        print('Não executado: OPENAI_API_KEY ausente. O curso principal roda offline.')
        return
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_openai import ChatOpenAI
    prompt=ChatPromptTemplate.from_messages([
        ('system','Responda em português, apenas com informações fornecidas. Não invente dados.'),
        ('human','Texto: {texto}\nPergunta: {pergunta}')])
    chain=prompt|ChatOpenAI(model='gpt-4.1-mini',temperature=0)|StrOutputParser()
    print(chain.invoke({'texto':'A receita da empresa fictícia foi de R$ 100 milhões.',
        'pergunta':'Qual foi a receita?'}))
if __name__=='__main__':main()
