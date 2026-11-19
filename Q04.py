numeros = [7, 12, 5, 18, 9, 20, 3, 14]

par = []
impar = []
for i in range(len(numeros)):
	if i % 2 == 0:
		par.append(i)
	else:
		impar.append(i)

print(f'Posições pares: {par}')
print(f'Posições ímpares: {impar}')