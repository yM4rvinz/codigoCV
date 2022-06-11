while True:
    print("Consoante(V) e vogais(V) e ambos(-)")
    listaR10 = [["c"], ["v"]]

    def possibilidadesCV():
        global listaFINAL
        global listaR10
        tamanho = codigoCV.count("-")
        y = 0
        x = 0
        w = 0
        globals()["listaR{}{}".format(y + 3, y)] = []

        def criarlista():
            globals()["listaR{}{}".format(y + 2, y)] = globals()["listaR{}{}".format(y + 1, y)] + globals()[
                "listaR{}{}".format(y + 1, y)]
            globals()["listaR{}{}".format(y + 3, y)].append(globals()["listaR{}{}".format(y + 2, y)][x].copy())
            globals()["listaR{}{}".format(y + 3, y)][x].append("c" if x < len(globals()["listaR{}{}".format(y+2, y)])/2 else "v")

        for b in range(0, 2 ** tamanho):
            if tamanho > 2:
                while tamanho - y != 1:
                    criarlista()
                    x += 1
                    if x == 2 * (2 ** (y + 1)):
                        y += 1
                        x = 0
                        globals()["listaR{}{}".format(y + 1, y)] = (globals()["listaR{}{}".format(y + 2, y - 1)])
                        globals()["listaR{}{}".format(y + 3, y)] = []
            elif tamanho == 1:
                globals()["listaR{}{}".format(3 + w, w)] = listaR10
            else:
                criarlista()
                x += 1
        if y != 0:
            w = y - 1
        listaFINAL = globals()["listaR{}{}".format(3 + w, w)]

    def pesquisarCV():
        global posicoesDASH
        global listaFINAL
        global numero_palavras
        lista_palavras = []
        codigosCVS = []
        todas_as_posicoes2 = []
        todas_as_posicoes3 = []
        palavras_normais = open("br-utf8.txt", "r", encoding="utf8").read().split()
        palavras_convertidas = open("lista_convertida.txt", "r").read().split()
        if "-" not in codigoCV:
            todas_as_posicoes = [i for i, p in enumerate(palavras_convertidas) if p == codigoCV]
            if len(todas_as_posicoes) < int(numero_palavras):
                print(
                    "ops!, parece que não existe essa quantidade de palavras. foram encontradas {} palavras que obedecem a esse código!".format(len(todas_as_posicoes)))
            else:
                for nm in range(0, int(numero_palavras)):
                    lista_palavras.append(palavras_normais[todas_as_posicoes[nm]])
            print("foram encontradas, ao todo, {} palavras, porém, {} foram exibidas".format(len(todas_as_posicoes), numero_palavras))
        else:
            posicoesDASH = [i for i, p in enumerate(codigoCV) if p == "-"]
            for mn in range(0, len(listaFINAL)):
                codigosCVS.append(list(codigoCV).copy())
            for nm in range(0, len(codigosCVS)):
                for nm1 in range(0, len(posicoesDASH)):
                    codigosCVS[nm][posicoesDASH[nm1]] = listaFINAL[nm][nm1]
                codigosCVS[nm] = "".join(codigosCVS[nm])
                todas_as_posicoes = [i for i, p in enumerate(palavras_convertidas) if p == codigosCVS[nm]]
                todas_as_posicoes2.append(todas_as_posicoes)
            for nm in range(0, len(todas_as_posicoes2)):
                todas_as_posicoes3 += todas_as_posicoes2[nm]
            if len(todas_as_posicoes3) < int(numero_palavras):
                print("ops!, parece que não existe essa quantidade de palavras. foram encontradas {} palavras que obedecem a esse código!".format(len(todas_as_posicoes3)))
            else:
                for nm in range(0, int(numero_palavras)):
                    lista_palavras.append(palavras_normais[todas_as_posicoes3[nm]])
                print("foram encontradas, ao todo, {} palavras, porém, {} foram exibidas".format(len(todas_as_posicoes3), numero_palavras))
        print(sorted(lista_palavras, key=str.lower))

    while True:
        codigoCV = input("digite o código de letras: ").lower().strip()
        if ("c" in codigoCV or "v" in codigoCV) and (not "-" in codigoCV):
            break
        elif "-" in codigoCV:
            possibilidadesCV()
            break
        else:
            print("você não digitou um código válido! tente novamente")

    while True:
        numero_palavras = input("digite o numero de palavras a ser procurado: ").strip()
        if numero_palavras.isdigit():
            pesquisarCV()
            break
        else:
            print("você não digitou um numero! tente novamente")