while True:
    nome = input('Qual o seu nome? ')
    if (nome != 'gabi'):
        continue #volta do inicio
    senha = input('Qual a sua senha? ')
    if (senha == 'caralho'):
        break #encerra o laço
print('Acesso concedido')