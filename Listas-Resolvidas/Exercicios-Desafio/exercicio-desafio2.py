'''Exercício 2:
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
nenhuma delas esteja em falta no caixa.'''

valor = int(input('Valor a pagar: R$ '))
recebido = int(input('Informe o valor fornecido pelo cliente: R$ '))

troco = recebido - valor
#encontrando quantas notas de 50 reais serão necessárias
notas50 = int(troco/50)
troco = troco % 50 
notas20 = int(troco/20)
troco = troco % 20
notas10 = int(troco/10)
troco = troco % 10
notas5 = int(troco/5)
troco = troco % 5
notas2 = int(troco/2)
notas1 = troco % 2

#Informando as notas necessárias para a(o) funcionária(o):
print('Troco:')
if notas50 > 0:
    print(f'{notas50} nota(s) de 50 reais.')
if notas20 > 0:
    print(f'{notas20} nota(s) de 20 reais.')
if notas10 > 0:
    print(f'{notas10} nota(s) de 10 reais.')
if notas5 > 0:
    print(f'{notas5} nota(s) de 5 reais.')
if notas2 > 0:
    print(f'{notas2} nota(s) de 2 reais.')
if notas1 > 0:
    print(f'{notas1} nota de 1 real.')