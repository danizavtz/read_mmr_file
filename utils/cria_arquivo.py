def gerar_arquivo(nome):
    f = open(nome, "w+")
    for i in range(999999999):
        f.write('{},{},{}\n'.format('Nome '+str(i),18,str(i)+'@abc.com'))

    f.close()