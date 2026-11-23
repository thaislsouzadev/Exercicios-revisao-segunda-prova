def eh_palindromo(palavra):
	copia_palavra = palavra
	lista = list(palavra)
	empilhar = []
	while lista:
		empilhar.append(lista.pop(0))
	
	desempilhar = []
	while empilhar:
		desempilhar.append(empilhar.pop())
		    
	if ''.join(desempilhar) == copia_palavra:
		print(True)
	else:
		print(False)

eh_palindromo('arara')
eh_palindromo('radar')
eh_palindromo('python')