#Fatorial de 10: 1 * 2 * 3 * (...) * 10

k = 1
fat = 1
numLido = int(input('Informe o número que você quer calcular o fatorial: '))

while k <= numLido:
    fat = fat * k
    k = k + 1

print(f'Fatorial de {numLido} é {fat}.')