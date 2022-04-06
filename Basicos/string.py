'''Alguns comandos interessantes de strings:
FATIAMENTO:
    x = '0123456789'
    print(x[0:2])
    saída esperada: 01
índices podem ser omitidos
    print(x[:2])
    saída esperada: 01
    print(x[4:])
    saída esperada:  456789
    print(x[4:-1])
    saída esperada: 45678
INCREMENTO DO FATIAMENTO
    texto = 'batatinha quando nasce'
    print(texto[::2])  <-- do início, pulando de 2 em 2
    print(texto[::-1]) <-- imprime string invertida!
'''

#Testar se é palíndromo (igual de trás pra frente)

palavra = input("Escreva uma palavra: ")
if palavra == palavra[::-1]:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')