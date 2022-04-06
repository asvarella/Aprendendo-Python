'''
Exercício 5:
Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
preço a pagar.
'''

preco = float(input('Informe o valor da mercadoria: '))
porcentagem = float(input('Informe o percentual de desconto: '))

desconto = (porcentagem/100) * preco

print(f'Valor do desconto: R$ {desconto: .2f}')
print(f'Total a pagar: R$ {(preco-desconto): .2f}')
