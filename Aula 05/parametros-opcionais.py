def soma3(x = 0,y = 0,z = 0):
    res = x + y + z
    print(res)

soma3(1, 2, 3)
soma3(1, 2)
soma3(1,)
soma3()

def borda(s1):
    tam = len(s1)
    if tam:
        print('+','-' * tam, '+')
        print('|', s1,'|')
        print('+','-' * tam, '+')

borda('Olá, Mundo!')
borda('Meu nome é Gabrielle da Silva Rodrigues')
