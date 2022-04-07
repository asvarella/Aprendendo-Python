'''OBS: EVITE NOMEAR ARQUIVOS "RANDOM.PY"
'''
import random

#escolhendo número aleatório em determinado intervalo
numero_aleatorio = random.randint(1,100)
print(numero_aleatorio)

#criando uma lista de nomes
nomes = ['zé', 'lia', 'joao', 'ruth']
print(nomes)

#escolhendo um nome aleatório da lista de nomes predeterminada
escolhido = random.choice(nomes)
print(escolhido)

#embaralhando a lista de nomes
random.shuffle(nomes)
print(nomes)

#usando a funçao sample:
lista_num = random.sample(range(100), 10) #10 números de 0 a 99(?)
print(lista_num)