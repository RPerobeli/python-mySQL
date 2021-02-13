#DataSus - populacao br entre 1080 até 2016
import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv", "r").readlines()
anos = []
populacao = []

for i in range(len(dados)):
    if (i != 0):
        linha = dados[i].split(";")
        anos.append(int(linha[0]))
        populacao.append(int(linha[1]))

plt.bar(anos,populacao, label = "Populacao")
plt.title("populacao br de 1980 a 2016")
plt.xlabel("anos")
plt.ylabel("populacao (em milhoes)")
plt.legend()
plt.show()
