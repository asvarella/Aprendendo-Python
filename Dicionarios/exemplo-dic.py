'''Temos um arquivo .txt com o livro inteiro de Alice no País das Maravilhas. 
Iremos criar um dicionário a partir das palavras do livro que mostra as 20 palavras mais frequentes e seus números de ocorrências.
'''
from audioop import reverse
import string

texto = open(r'Aprendendo-Python\files\alice.txt').read().lower() #abre o arquivo, lê na variável texto com todas as letras em lowercase.
for c in string.punctuation:
    texto = texto.replace(c, ' ') #remove caracteres especiais

palavras = texto.split() #separa o texto em lista de palavras

#dicionario word_count:
wc = {}

for p in palavras:
    if p in wc: #testa se palavra já foi adicionada ao dicionário
        wc[p] += 1 #adiciona 1 à contagem da palavra
    else:
        wc[p] = 1 #primeira incidência da palavra

def contador(dupla):
    return dupla[1]

#organizando as duplas (palavra, no. ocorrências) por ordem de numero de ocorrências
duplas = sorted(wc.items(), key = contador, reverse = True)
for dupla in duplas[:20]:
    print(dupla[0], dupla[1])
