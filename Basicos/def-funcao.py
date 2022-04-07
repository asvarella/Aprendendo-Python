def fatorial(x):
    fat = 1
    for k in range(1,x+1): #lembrar que range de x, por padrão, vai até x-1!
        fat = fat * k
    return fat

entrada = int(input('Digite um número para calcular o fatorial: '))
print(fatorial(entrada))