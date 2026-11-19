precos = [12.0, 45.0, 8.5, 60.0, 30.0, 5.0]

precos_ajustados = []

for i in range(len(precos)):
	if precos[i] >= 30:
		precos_ajustados.append(precos[i]-precos[i]*0.1)
	elif i % 2 != 0:
		precos_ajustados.append(precos[i] + 2)
	else:
		precos_ajustados.append(precos[i])

print(precos_ajustados)