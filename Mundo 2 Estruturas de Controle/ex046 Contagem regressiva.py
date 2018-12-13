# Fa�a um programa que mostre na tela uma contagem regressiva para estouro de fogos de artif�cio, indo de 10 at� 0, com uma pausa de 1 segundo entre eles.








from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM ! BUM ! POOOW!')