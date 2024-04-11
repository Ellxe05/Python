#CONCATENAÇAO
s1 = 'Lógica de Programação'
s1 = s1 + ' e Algorítmos.'
print(s1)

#REPETINDO STRINGS NA CONCATENAÇAO
s1 = 'A' + '-' * 10 + 'B'
print(s1)

s1 = 'A' + ' ' * 10 + 'B'
print(s1)

#COMPOSIÇAO POR MARCADOR DE POSIÇAO
nota = 9.0
s1 = 'Você tirou %f na disciplina de Algorítmos' % nota 
print(s1)

#LIMITANDO AS CASAS DECIMAIS
nota = 9.5
s1 = 'Você tirou %.2f na disciplina de Algorítmos' % nota
print(s1)

#VARIAS VARIAVEIS
nota = 9.2
disciplina = 'Algorítmos'
s1 = 'Você tirou %.2f na disciplina de %s' % (nota, disciplina)
print(s1)

#COMPOSIÇAO MODERNA
nota = 8.5
disciplina = 'Algorítmos'
s1 = 'Você tirou {} na disciplina {}' .format(nota, disciplina)
print(s1)

#COMPOSIÇAO COM F-STRING
nota = 8.2
disciplina = 'Algorítmos'
s1 = f'Você tirou {nota} na disciplina de {disciplina}.'
print(s1)

#FATIAMENTO
s1 = 'Lógica de Programação e Algoritmos'
print(s1[0:6])
s1 = 'Lógica de Programação e Algoritmos'
print(s1[24:34])
s1 = 'Lógica de Programação e Algoritmos'
print(s1[10:22])

#TAMANHO (LENGTH)
s1 = 'Lógica de Programação e Algoritmos'
tamanho = len(s1)
print(tamanho)