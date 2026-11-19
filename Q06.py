quilos = 1
contador_doacoes = 0
soma = 0

while quilos != 0:
	quilos = float(input('Quilos doados (0 para encerrar)'))

	if quilos < 0:
		print('DOAÇÃO INVÁLIDA')
	elif quilos > 0:
		soma += quilos
		contador_doacoes += 1

print(f'Quantidade de doações: {contador_doacoes}')
print(f'Total arrecadado: {soma}')

if soma >= 50:
	print('META DA CAMPANHA ATINGIDA')
else:
	falta = 50 - soma
	print(f'Falta {falta}kg para a meta')