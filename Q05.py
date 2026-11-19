contador_carros = 0
soma = 0
horas = 1
while horas != 0:
	horas = int(input('Horas de permanência (0 para encerrar)'))
	if horas > 0 and horas < 24:
		total = horas * 5
		soma += total
		contador_carros += 1
	elif horas < 0 or horas > 24:
		print('VALOR INVÁLIDO')


print(f'Carros atendidos: {contador_carros}')
print(f'Total arrecadado: {soma}')
if total > 200:
	print('Bom dia')