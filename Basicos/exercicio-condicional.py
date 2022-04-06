'''
Pergunte a velocidade de um carro, supondo um valor inteiro. Caso ultrapasse 110 km/h, exiba uma mensagem dizendo que o usuário foi multado. Neste caso, exiba o valor da multa, 
cobrando R$ 5,00 por km acima de 110
'''
vel = int(input('Informe a velocidade atingida pelo carro: '))
if(vel <= 110):
    print('O carro apresentou velocidade adequada para a via. Nenhuma ação necessária')
else:
    diff = vel - 110
    print(f'O dono do carro deverá pagar uma multa de R$ {5*diff: .2f}')