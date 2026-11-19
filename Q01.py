lista = [4, 9, 15, 22, 30, 7]

nova_lista = []
for i in range(len(lista)):
	if lista[i] % 3 == 0:
		nova_lista.append(lista[i]//3)
	elif lista[i] % 3 != 0 and i % 2 == 0:
		nova_lista.append(lista[i] + i)
print(nova_lista)