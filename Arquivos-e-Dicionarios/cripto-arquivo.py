#Abre o arquivo de message.txt em modo de leitura.
#Cria o arquivo cripto.txt que apresenta a mesma mensagem com * no lugar das vogais

mensagem = open(r'Aprendendo-Python\files\message.txt', 'r')
cripto = open(r'Aprendendo-Python\files\cripto.txt', 'w')
for linha in mensagem.readlines(): #lê cada linha de mensagem.txt
    for letra in linha:            #percorre cada palavra em cada linha do texto
        if letra in 'aeiouãáeíõóéàôêâ':
            cripto.write('*')
        else:
            cripto.write(letra)

mensagem.close()
cripto.close()