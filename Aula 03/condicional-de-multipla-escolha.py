print('Tabela de preços: maçã) R$2.30 - laranja) R$3.60 -  banana) R$1.85')

print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')

fruta = int(input('O que vai comprar? '))
unid = int(input('Quantas unidades? '))

if (fruta == 1): #maça
    pagar = unid * 2.3
    print(f'Você comprou {unid} maçãs. Total à pagar: {pagar}')
elif (fruta == 2): #laranja
    pagar = unid * 3.6
    print(f'Você comprou {unid} laranjas. Total à pagar: {pagar}')
elif (fruta == 3): #banana
    pagar = unid * 1.85
    print(f'Você comprou {unid} maçãs. Total à pagar: {pagar}')
else:
    print('Produto inexistente!')

#EXERCICIO
nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))

if nome == 'Gabrielle':
    print('Olá, Gabrielle!')
elif idade < 18:
    print('Você não é a Gabrielle, e é menor de idade!')
elif idade > 100:
    print('Diferente de você, a Gabrielle não é imortal!')
        