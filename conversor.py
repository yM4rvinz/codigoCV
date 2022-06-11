import unidecode

x = 0
y = -1
z = 0
todas_palavras = open("br-utf8.txt", "r", encoding="utf8")
lista_palavras = todas_palavras.read().split()
palavra = ""
palavra_convertida = ""
palavra_separada = []
lista_final_convertida = []

def converter():
    global x
    global palavra_convertida
    
    def proxima_palavra():
        global lista_palavras
        global y
        global palavra_separada
        y += 1
        palavra = unidecode.unidecode((lista_palavras[y]).lower())
        palavra_separada = list(palavra)
    proxima_palavra()

    while x != len("".join(palavra_separada)):
        if palavra_separada[x] in vogais:
            palavra_separada[x] = "v"
            x += 1
        elif palavra_separada[x] in consoantes:
            palavra_separada[x] = "c"
            x += 1
    palavra_convertida = "".join(palavra_separada)
    lista_final_convertida.append(palavra_convertida)
    x = 0

while len(lista_palavras) != z:
    converter()
    z += 1

with open("lista_convertida.txt", "w") as f:
    f.write(str(" ".join(lista_final_convertida)))