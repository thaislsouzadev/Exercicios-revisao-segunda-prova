cont_pares = 0
cont_impares = 0
numero = 1
max = 0

while numero != 0:
    numero = int(input('Número inteiro positivo (0 para encerrar): '))
    if numero > 0:
        if numero > max:
            max = numero
        if numero % 2 == 0:
            cont_pares += 1
        else:
            cont_impares += 1
    else:
        print('')

print(f'Pares: {cont_pares}')
print(f'Impares: {cont_impares}')
print(f'Maior número: {max}')