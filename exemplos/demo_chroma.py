"""Chroma local com embedding hash didático NÃO SEMÂNTICO; para aprender API/coleções."""
import hashlib
import numpy as np

def vector(text):
    x=np.zeros(32,dtype='float32')
    for word in text.lower().split():
        h=int(hashlib.sha256(word.encode()).hexdigest(),16)
        x[h%32]+=1
    n=np.linalg.norm(x)
    return (x/n if n else x).tolist()

def main():
    import chromadb
    client=chromadb.EphemeralClient()
    coll=client.get_or_create_collection('catalogo_exemplo')
    texts=['mochila para notebook','copo térmico para café','bolsa para computador']
    coll.add(ids=['p1','p2','p3'],documents=texts,embeddings=[vector(t) for t in texts])
    print(coll.query(query_embeddings=[vector('bolsa computador')],n_results=2))
    print('ATENÇÃO: vetores hash não representam significado; resultado apenas ilustra a API.')
if __name__=='__main__':main()
