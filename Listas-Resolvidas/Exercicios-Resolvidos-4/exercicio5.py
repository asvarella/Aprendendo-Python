'''Exercício 5
Seja o mesmo texto [exercício 4] “splitado”. Calcule quantas palavras possuem uma das letras
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
minúsculas e de remover antes os caracteres especiais.
'''
import string

#função que encontra algum dos caracteres de 'python' em uma palavra:
def tempython(palavra):
    for c in palavra:
        if c in 'python':
            return True
        else:
            return False

#string sem uppercase:
texto = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'.lower()

#Removendo caracteres especiais:
for c in string.punctuation:
    texto = texto.replace(c, '')

#resposta = [] <- string de teste para ver a resposta dada pelo problema
count = 0 #contador de palavras

for i in texto.split():
    if tempython(i) and len(i) > 4:
        #resposta.append(i)
        count = count + 1

#print(resposta)        
print(count)