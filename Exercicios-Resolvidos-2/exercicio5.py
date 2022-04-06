'''Exercício 5:
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
num3 = int(input('Numero 3: '))

if ((num1 > num2) and (num1 > num3)):
    print (f'Maior número = {num1}')
    if(num2 > num3):
        print (f'Menor número = {num3}')    
    else:
        print (f'Menor número = {num2}')
elif((num2 > num1) and (num2 > num3)):
    print (f'Maior número = {num2}')
    if(num1 > num3):
        print (f'Menor número = {num3}')    
    else:
        print (f'Menor número = {num1}')
else:
    print (f'Maior número = {num3}')
    if(num2 > num1):
        print (f'Menor número = {num1}')    
    else:
        print (f'Menor número = {num2}')