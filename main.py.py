# tempo de importação

# ini = time.time()
def permutações (l):
    se len(l) == 1:
        retornar [l]

    listaAuxiliar | = []

    para o índice no intervalo[len(l)):
        k = l[índice]

        listaSemK = l[:indice] + l[indice + 1:]

        para p em permutações (listaSemK):
            listaAuxiliar. append([k] + p)
    return listaAuxiliar


file = open('matriz6.txt', 'r')
i, j = arquivo. readline(). fender()
linhas = arquivo. read(). linhas divisas()
coordenadas = {}
listaDePontos | = []

para c na gama[int(i)):
    cadaLinha = linhas[c]. fender()
    para o ponto em cadaLinha:
        if ponto != '0':
            coordenadas[ponto] = (c, cadaLinha. index(ponto))
            listaDePontos. append(ponto)

listaDePontos. remove('R')
menorCusto = float('inf')
permut = list(permutations(listaDePontos))

para caminho in permut:
    custódiaTotal = 0
    indiceDeSoma = 0

    caminho = list(caminho )
    caminho. append('R')
    caminho. insert(0, 'R')

    enquanto indiceDeSoma < len(caminho)-1:
        custoX = abs(coordenadas[caminho[indiceDeSoma]][0] - coordenadas[caminho[indiceDeSoma + 1]][0])
        custoY = abs(coordenadas[caminho[indiceDeSoma]][1] - coordenadas[caminho[indiceDeSoma + 1]][1])
        custoTotal += custoX + custódia
        indiceDeSoma += 1

    se a custódiaTotal < menorCusto:
        menorCusto = custoTotal
        menorCaminho = caminho
resultado = ' '. junte(menorCaminho[1:-1])
print(resultado)


# fim = time.time()
# tempo = fim-ini
# impressão(tempo)