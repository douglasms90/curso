# Desenvolva uma l�gica que leia o peso altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 at� 30: Sobrepeso
# 30 at� 40: Obesidade
# Acima de 40: Obesidade m�rbida


peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc >= 40:
    print ('Obesidade')
else:
    print('Obesidade morbida')