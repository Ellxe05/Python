soma = 0 
cont = 1

while (cont <= 5):
    x = int(input(f'Digite o {cont}ª número: '))
    soma += x
    cont += 1
print(f'Somatório: {soma}')