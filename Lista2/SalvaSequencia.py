
arq = open("FASTA.txt", 'a')
cabecalho = input("Digite o cabeçalho FASTA: ")
seq = input("Digite a sequencia: ")

arq.write('>'+cabecalho+'\n')
arq.write(seq+'\n')


