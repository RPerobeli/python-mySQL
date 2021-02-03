arquivo = open("FASTA.txt")
linhas = arquivo.readlines()
multifasta = {}
for linha in linhas:
    if linha[0] == ">":
        seqAtual = linha.strip()
        multifasta[seqAtual] = ""
    else:
        #concatena pois ele vai ler diversas linhas de sequencia
        multifasta[seqAtual] = multifasta[seqAtual]+linha.strip()

print(multifasta)