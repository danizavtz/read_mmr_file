from utils.cria_arquivo import gerar_arquivo
from models.pessoa import Pessoa


def inserir(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True 
            break
    if key_exists:
        bucket[i][1][1] += 1
    else:
        bucket.append((key, [value,1]))

def main():
    print('criando arquivo 1')
    gerar_arquivo('exemplo1.txt')
    print('criando arquivo 2')
    gerar_arquivo('exemplo2.txt')
    #le o conteudo do primeiro arquivo
    f = open('exemplo1.txt','r')
    conteudo = f.readlines()
    f.close()
    #cria uma hashtable com o dobro do tamanho do primeiro arquivo
    hash_table = [[] for _ in range(2*len(conteudo))]
    for l in conteudo:
        arr = l.split(',')
        p = Pessoa(arr[0],arr[1],arr[2])
        inserir(hash_table, hash(p.nome), p)
    
    f = open('exemplo2.txt', 'r')
    for l in f:
        arr = l.split(',')
        p = Pessoa(arr[0],arr[1],arr[2])
        inserir(hash_table, hash(p.nome), p)
    f.close()
    
    # print(len(hash_table))
    # print(hash_table)

if __name__ == '__main__':
    main()