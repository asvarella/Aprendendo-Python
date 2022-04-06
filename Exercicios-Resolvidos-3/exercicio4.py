'''Exercício 4:
A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
'''

entrada = int(input('Entrada: '))
k = 1
f1 = f2 = 1
fibo = 0
while k <= entrada:
    if (k == 1 or k == 2):
        fibo = 1
    else:
        fibo = f2 + f1
        f1 = f2
        f2 = fibo
    print(f'F{k} = {fibo}')
    k = k + 1

        