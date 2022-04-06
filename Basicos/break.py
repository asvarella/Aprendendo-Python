#Repetições sem definição de parada

soma = 0
numElementos = 0

while True:
    x = int(input('Informe um número: '))
    if (x == 0):
        break
    else:
        soma = soma + x
        numElementos = numElementos + 1

print(f'Soma: {soma}')
media = soma/numElementos
print(f'Media dos valores inseridos: {media}')