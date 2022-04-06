'''Exercício 2:
Determine se um ano é bissexto. Verifique no Google como fazer isso...
    
    ANO BISSEXTO: "Qualquer ano que seja uniformemente divisível por 4 é um ano bissexto"
    No entanto, ainda há um pequeno erro que deve ser contabilizado. 
    Para eliminar esse erro, o calendário gregoriano estipula que um ano que é uniformemente divisível por 100 (por exemplo, 1900) é um ano bissexto apenas se também é igualmente divisível por 400.
    Por essa razão, os seguintes anos não são bissextos: 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600:
    Isso porque eles são uniformemente divisíveis por 100, mas não por 400.

    olhar função isleaf de python
'''

ano = int(input('Digite o ano: '))

if(ano % 4 == 0):
    if((ano % 100 == 0) and (ano % 400 != 0)):
        print ('Este não é um ano bissexto.')
    else:
        print ('Este é um ano bissexto')
else:
    print ('Este não é um ano bissexto.')
