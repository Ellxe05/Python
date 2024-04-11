#FUNÇAO DE ENTRADA
idade = input('Qual sua idade? ')
print(idade)
nome = input('Qual seu nome? ')
print(f'Olá {nome}, seja bem-vindo!')

#CONVERTENDO DADOS DE ENTRADA (CASTING)
nota = float(input('Qual nota você recebeu na disciplina?'))
print(f'Você tirou nota {nota}.')

#FLUXO DE EXECUÇAO DO PROGRAMA (TESTE DE MESA)
x = 1
y = 1
z = x + y # z = 2

x = x + 2 # x = 3
y = y - 1 # y = 0
z = x + y # 3 + 0 = 3

x = y + 1 # x = 1
y = x - 1 # y = 0
z = x + y # z = 1

print(z) # z = 1

#EXERCICIO
num1 = int(input('Escolha um número inteiro.'))
num2 = int(input('Escolha um segundo número inteiro.'))
soma = num1 + num2
print(f'A soma dos números {num1} e {num2} é: {soma}')