'''
Exercício 4:
Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
'''
salario = float(input('Informe o salário original: '))
porcentagem = float(input('Informe o percentual de aumento: '))

aumento = (porcentagem/100) * salario

print(f'Aumento calculado: R$ {aumento: .2f}')
print(f'Novo salário: R$ {salario+aumento: .2f}')
