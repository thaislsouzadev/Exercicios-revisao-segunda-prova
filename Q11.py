def profundidade(expressao):
    pilha = []
    max = 0
    for i in expressao:
        if i == '(':
            pilha.append('(')
            if len(pilha) > max:
                max = len(pilha)
        elif i == ')':
            pilha.pop()
    return max

a = profundidade('(a+b) * (c-d)')
b = profundidade('((a+b) * (c-(d+e)))')
c = profundidade('a+b')

print(f'{a} {b} {c}')