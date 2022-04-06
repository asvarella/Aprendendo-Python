'''Exercício 1:
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

invalido = True

while invalido:
    nota = int(input('Insira uma nota de 0 a 10: '))
    if(nota < 0 or nota > 10):
        print('Valor inválido. Digite novamente.')
    else:
        invalido = False

print(f'A nota que você deu é {nota}')