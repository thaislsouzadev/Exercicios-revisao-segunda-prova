def soma_matriz(a, b):
    nova_matriz = []
    lista = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            lista.append(a[i][j] + b[i][j])
        nova_matriz.append(lista)
        lista = []
    
    print(nova_matriz)

soma_matriz([[1 ,2] , [3, 4]] , [[10, 20], [30, 40]])
soma_matriz([[1, 0, 2]], [[5, 5, 5]])