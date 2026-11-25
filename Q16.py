def identidade(n):
    matriz = []
    lista = []
    for i in range(n):
        for j in range(n):
            if i == j:
                lista.append(1)
            elif i != j:
                lista.append(0)
        matriz.append(lista)
        lista = []
    print(matriz)

identidade(3)