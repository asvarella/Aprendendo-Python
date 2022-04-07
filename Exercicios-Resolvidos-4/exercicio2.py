'''Exercício 2:
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
números ímpares na lista IMPAR. Imprima as três listas.
'''

import random

lista = random.sample(range(1,101), 20)

#LISTAS VAZIAS: lembre-se de usar o método 'nomelista'.append() para adicionar elementos
par = []
impar = []

for i in range(20):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])

print('Lista de números gerada:\n', lista)
print('Lista de números pares:\n', par)
print('Lista de números ímpares:\n',impar)