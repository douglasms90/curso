# Estreva um programa que leia um valor em metros e a exiba convertido em centímetros e milímetros.








medida = float(input('Uma distancia em metros:'))
cm = medida * 100
mm = medida * 1000
print('A media de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
