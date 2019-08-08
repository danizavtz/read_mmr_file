def gerar_arquivo(nome):
    f = open(nome, "w+")
    for i in range(9999):
        f.write('{},{},{}\n'.format('Nome '+str(i),18,str(i)+'@abc.com'))

    f.close()

def ler_arquivo_por_linha(nome):
    with open(nome) as arquivo_por_linha:
        linha = arquivo_por_linha.readline()
        while linha:
            # print(linha.strip)
            arr = linha.split(',')
            print(arr)
            linha = arquivo_por_linha.readline()