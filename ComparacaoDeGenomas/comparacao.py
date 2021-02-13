humano = open("18s_humano.fasta", "r").read()
bacteria = open("16s_bacteria.fasta", "r").read()

saida_bacteria = open("bacteria.html", "w")
saida_humano = open("humano.html", "w")

humano = humano.replace("\n","")
bacteria = bacteria.replace("\n","")

nucleotideosHumano = {}
nucleotideosBacteria = {}
nucleotideos = ['A','T','C','G']

#cria um dicionario zerado com todas as 16 combinações de nucleotideos
for i in nucleotideos:
    for j in nucleotideos:
        nucleotideosHumano[i+j] = 0
        nucleotideosBacteria[i+j] = 0

for k in range(len(humano)-1):
    nucleotideosHumano[humano[k]+humano[k+1]] += 1

for l in range(len(bacteria)-1):
    nucleotideosBacteria[bacteria[l]+bacteria[l+1]] += 1

#html
cont =1 
for k in nucleotideosHumano:
    transparencia = nucleotideosHumano[k]/max(nucleotideosHumano.values())
    saida_humano.write("<div style= 'width:100px; bordr:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0,0,0,"+str(transparencia)+"')>"+str(k)+"</div> ")
    if(cont%4 == 0):
        saida_humano.write("<div style='clear: both'></div>")
    cont+=1
saida_humano.close()
cont = 1
for k in nucleotideosBacteria:
    transparencia = nucleotideosBacteria[k]/max(nucleotideosBacteria.values())
    saida_bacteria.write("<div style= 'width:100px; bordr:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0,0,0,"+str(transparencia)+"')>"+str(k)+"</div> ")
    if(cont%4 == 0):
        saida_bacteria.write("<div style='clear: both'></div>")
    cont+=1
saida_bacteria.close()