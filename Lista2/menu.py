import sys
def LeArquivo(nome):
    arq = open(nome, 'r')
    texto = arq.read()
    arq.close()
    return texto

def AddDicionario(dicionario,cab, seq):
    if(dicionario.get(cab)):
        print("Já existe esse cabecalho.")
        resp = input("Deseja substituir?(s/n)")
        if(resp.lower == "s"):
            dicionario[cab] = seq
        else:
            print("Não foi adicionado ao dicionario.")
    else:
        dicionario[cab] = seq

def LeMultiFasta(nome):
    arq = open(nome, 'r')
    dictFASTA = {}
    for linha in arq:
        valores = linha.split()
        AddDicionario(dictFASTA, valores[1],valores[2])
    return dictFASTA
    
    

continuar = True
txt = ""
while continuar == True:
    print("Menu:")
    print("1 - Ler arquivo texto.")
    print("2 - Exibir o texto lido.")
    print("3 - Sair do programa.")
    print("4 - Lê arquivo MULTIFASTA")
    entrada = input("Digite o que deseja fazer:")
    if(entrada == "1"):
        arquivo = input("Digite o nome do arquivo a ser lido(com extensão): ")
        txt = LeArquivo(arquivo)
    elif(entrada == "2"):
        print("O texto do arquivo é: ")
        print(txt)
    elif(entrada == "3"):
        continuar = False
    elif(entrada == "4"):
        arquivo = input("Digite o nome do arquivo multifasta: ")
        dicionario = LeMultiFasta(arquivo)
        print(dicionario)
    else:
        print("Entrada inválida.")


sys.exit()