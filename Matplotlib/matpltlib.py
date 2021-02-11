import matplotlib.pyplot as plt

#grafico de linhas
# x = [1,2,5]
# y = [2,3,7]
# titulo = "Meu prim grafico com python"
# eixox = "eixo x"
# eixoy = "eixo y"
# plt.title(titulo)
# plt.xlabel(eixox)
# plt.ylabel(eixoy)
# plt.plot(x,y)
# plt.show()

# #grafico de barras
# x = [1,3,5,7,9]
# y = [2,3,7,1,0]
# x1 = [2,4,6,8,10]
# y1 = [5,1,3,7,4]
# titulo = "Barras 2"
# eixox = "eixo x"
# eixoy = "eixo y"
# plt.title(titulo)
# plt.xlabel(eixox)
# plt.ylabel(eixoy)
# p1 = plt.bar(x,y, label = "grupo 1")
# p2 = plt.bar(x1,y1, label = "grupo 2")
# # plt.legend((p1[0],p2[0]), ("Grupo 1", "Grupo 2"))
# plt.legend()
# plt.show()

#grafico de dispersao
x = [1,3,5,7,9]
y = [2,3,7,1,0]
titulo = "Scatterplot"
eixox = "eixo x"
eixoy = "eixo y"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
p1 = plt.scatter(x,y, label = "grupo 1", color = "red", marker = "*")
plt.legend()
plt.show()


'''
color: cor (ver exemplos abaixo)
label: rótulo
linestyle: estilo de linha (ver exemplos abaixo)
linewidth: largura da linha
marker: marcador (ver exemplos abaixo)

CORES (color)
'b' blue
'g' green
'r' red
'c' cyan
'm' magenta
'y' yellow
'k' black
'w' white

Marcadores (marker)
'.' point marker
',' pixel marker
'o' circle marker
'v' triangle_down marker
'^' triangle_up marker
'<' triangle_left marker
'>' triangle_right marker
'1' tri_down marker
'2' tri_up marker
'3' tri_left marker
'4' tri_right marker
's' square marker
'p' pentagon marker
'*' star marker
'h' hexagon1 marker
'H' hexagon2 marker
'+' plus marker
'x' x marker
'D' diamond marker
'd' thin_diamond marker
'|' vline marker
'_' hline marker

Tipos de linha (linestyle)
'-' solid line style
'--' dashed line style
'-.' dash-dot line style
':' dotted line style
Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
'''