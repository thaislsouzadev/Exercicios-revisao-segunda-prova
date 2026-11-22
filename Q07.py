nota = 0
contador_validas = 0
contador_media = 0
soma = 0

while nota != -1:
    nota = float(input('Nota (-1 para encerrar): '))
    if nota >= 0 and nota <= 10:
        soma += nota
        contador_validas += 1
        if nota >= 7:
            contador_media += 1
    elif nota < -1 or nota > 10:
        print('NOTA INVÁLIDA')

if contador_validas == 0:
    print('NENHUMA NOTA REGISTRADA')
else:
    print(f'Média: {soma / contador_validas}')
    print(f'Notas maiores ou iguais a 7: {contador_media}')