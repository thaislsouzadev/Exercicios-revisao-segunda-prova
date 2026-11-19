temperaturas = [25, 27, 26, 30, 31, 29, 33]

posicoes = []
maior = temperaturas[0]
for i in range(len(temperaturas)):
	if temperaturas[i] > maior:
		posicoes.append(i)
		maior = temperaturas[i]

print(posicoes)
	