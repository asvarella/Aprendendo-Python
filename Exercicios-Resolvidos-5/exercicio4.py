'''Exercício 4:
Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
sortudos existem entre 18644 e 33087, incluindo os extremos?
'''

#criando funcao booleana para o exercicio
def numero_sortudo(numero):
    str_num = str(numero)
    if '2' in str_num:
        if '7' in str_num:
            return False
        else:
            return True
    else:
        return False

count_sortudos = 0 #para cada sortudo incrementa 1
for i in range(18644, 33088):
    if numero_sortudo(i):
        count_sortudos = count_sortudos + 1
print('Contagem de sortudos: ', count_sortudos)