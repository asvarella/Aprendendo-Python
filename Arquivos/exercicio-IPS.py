'''Programa que verifica se os endereços de IP são válidos ou não
Cria dois arquivos de saída, um com válidos e outro com inválidos.

CONDIÇÃO: CADA UM DOS BYTES DEVE SER MENOR QUE 255.'''

def ip_valido(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True


#abrindo o arquivo ips
ips = open(r'Aprendendo-Python\files\IPS.txt', 'r')
#criando arquivos de saída
validosIPS = open(r'Aprendendo-Python\files\validosIPS.txt', 'w')
invalidosIPS = open(r'Aprendendo-Python\files\invalidosIPS.txt', 'w')

for linha in  ips.readlines():
    if ip_valido(linha):
        validosIPS.write(linha)
    else:
        invalidosIPS.write(linha)

ips.close()
validosIPS.close()
invalidosIPS.close()

print('Processo finalizado.')