# Escreva um programa que leia a velocidade de um
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.






velocidade = float(input('Diga a velocidade:'))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Bom dia! Dirija com segurança!')