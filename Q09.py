def inverter(lista):
	empilhar = []
	while lista:
		empilhar.append(lista.pop(0))
	
	desempilhar = []
	while empilhar:
		desempilhar.append(empilhar.pop())

	print(f'Desempilhada {desempilhar}')


inverter([1, 2, 3, 4])
inverter(['a', 'b', 'c'])

