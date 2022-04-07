'''Exercício 6:
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
'''

ganhoHora = float(input('Informe quanto você ganha por hora: '))
horasTrab = float(input('Informe quantas horas trabalhadas no mês: '))

salBruto = ganhoHora * horasTrab
ir = salBruto * 0.11
inss = salBruto * 0.08
sind = salBruto * 0.05
salLiq = salBruto - ir - inss - sind

print (f'Salário Bruto: R$ {salBruto: .2f}\nIR: R$ {ir: .2f}\nINSS: R$ {inss: .2f}\nSindicato: R$ {sind: .2f}\nSalário Líquido: R$ {salLiq: .2f}')
