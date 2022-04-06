'''Exercício 2:
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

invalido = True

while invalido:
    usuario = input('Usuário: ')
    senha = input('Senha: ')
    if (senha == usuario):
        print('Senha inválida. Não utilizar senha igual ao nome de usuário.')
    else:
        invalido = False

print('Logado com sucesso.')