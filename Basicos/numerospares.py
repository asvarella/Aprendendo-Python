#Imprimir apenas números pares

x = 1
max = int(input('Max: '))

while (x <= max):
    if(x % 2 == 0):
        print(x)
    x = x + 1