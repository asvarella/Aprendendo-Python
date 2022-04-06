'''Ler uma string do tipo dd/mm/aaaa 
Escrever o mês por extenso.
'''
calendario = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro']

data = input('Informe a data no formato dd/mm/aaaa: ')
data = data.split('/')
num = int(data[1])
print (f'{calendario[num-1]}')


