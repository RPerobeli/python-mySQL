from random import randint

lista = []
for i in range(0,20):
    lista.append(randint(0,60))
print(lista)
lista.sort()
print(lista)