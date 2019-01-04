# Crie um programa onde o usu�rio digite uma express�o qualquer que use par�nteses. Seu aplicativo dever� analisar se a express�o passada est� com os par�nteses abertos e fechados na ordem correta.








expr = str(input('Digite a expressão: '))
pilha = list()
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')