#Exemplo 1:
'''
Considere a empresa de telefonia Tchau. Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto. Entre 200 e 400 minutos, o preço é R$ 0,18. Acima de 400 minutos o preço por minuto é
R$ 0,15. Calcule sua conta de telefone.
'''
#Exercicio extra: Modifique o programa da empresa Tchau para uma promoção onde a tarifa é de R$ 0,08 quando você utiliza mais que 800 minutos

tempo_total = int(input('Informe o tempo total de atividade ao telefone: '))

#Solução Exemplo 1:
'''
if (tempo_total < 200):
    custo_final = tempo_total * 0.20
else:
    if(tempo_total <= 400):
        custo_final = tempo_total * 0.18
    else:
        custo_final = tempo_total * 0.15
'''
#Solução Exercicio Extra:
if(tempo_total < 200):
    custo_final = tempo_total * 0.20
else:
    if(tempo_total <= 400):
        custo_final = tempo_total * 0.18
    elif(tempo_total > 800):
        custo_final = tempo_total * 0.08
    else:
        custo_final = tempo_total * 0.15

print(f'Sua conta de telefone apresenta uma cobrança de R$ {custo_final: .2f}')