from random import randint

def Aprovacao(nota):
    if(nota>=6):
        return "Aprovado"
    else:
        return "Reprovado"

notas = []
for i in range(0,10):
    notas.append(randint(0,10))
print(notas)

situacaoFinal = list(map(Aprovacao,notas))

print(situacaoFinal)

