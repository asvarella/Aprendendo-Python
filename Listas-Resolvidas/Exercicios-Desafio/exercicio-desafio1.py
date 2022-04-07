'''Exercício Desafio 1:
Dizemos que um número natural é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
verificar se n é triangular.'''

n1,n2,n3 = 1,2,3
#recebendo número n não-negativo
negativo = True
while negativo:
    n = int(input('Número: '))
    if n >= 0:
        negativo = False

#descobrindo se n é triangular
calculando = True
while calculando:
    if(n1*n2*n3 == n):
        print(f'{n} é triangular!')
        calculando = False
    elif(n1*n2*n3 > n):
        print(f'{n} não é triangular!')
        calculando = False
    else:
        n1,n2,n3 = n2,n3,n3+1