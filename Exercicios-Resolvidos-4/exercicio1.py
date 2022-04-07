'''Exercício 1:
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
as funções max e min.'''

import random

nums = random.sample(range(1,101), 10)

#variáveis para guardar o maior e o menor número
maior = -1
menor = 101

print(nums) #mostrando a lista gerada para testar se os dados estão sendo calculados corretamente

for i in range (10):
    if nums[i] > maior:
        maior = nums[i]
    if nums[i] < menor:
        menor = nums[i]

print('Maior número: ', maior)
print('Menor número: ', menor)