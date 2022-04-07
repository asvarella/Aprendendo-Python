'''Exercício 3:
Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores. Imprima os três vetores.'''

from operator import concat
import random

vetor1 = random.sample(range(1,101), 10)
vetor2 = random.sample(range(1,101), 10)

print('Vetor 1: ', vetor1)
print('Vetor 2: ', vetor2)

concatenado = []

#para cada iteração, dois valores adicionados ao vetor = 20 itens, intercalando vetor1 e vetor2.
for i in range (10):
    concatenado.append(vetor1[i])
    concatenado.append(vetor2[i])

print('Vetor 3: ', concatenado)