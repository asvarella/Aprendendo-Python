#Código que soma dez inteiros lidos

n = 1
soma = 0

while (n <= 10):
    x = int(input('Numero: '))
    soma = soma + x
    n = n + 1

print (f'Soma: {soma}')
#calcule a média dos dez números
media = soma/10
print (f'Média: {media}')
