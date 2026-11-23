def intercalar(fila1 , fila2):
    copia_fila1 = fila1.copy()
    copia_fila2 = fila2.copy()

    intercalar = []
    while copia_fila1 or copia_fila2:
        if len(copia_fila1) > 0:
            intercalar.append(copia_fila1.pop(0))
        if len(copia_fila2) > 0:
            intercalar.append(copia_fila2.pop(0))
    print(intercalar)

intercalar(['Ana', 'Carla', 'Elisa'] , ['Bruno', 'Diego'])
intercalar([1, 3] , [2, 4, 6, 8])