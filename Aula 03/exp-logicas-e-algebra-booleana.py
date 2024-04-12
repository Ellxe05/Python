#NOT
a = True
b = False
print(not a)
print(not b)

#AND
a = True
b = True
print(a and b)

#OR
a = True
b = False
print(a or b)

#EXPRESSOES LOGICAS/BOOLEANAS
x = 10
y = 1
res = not x > y
print(res)

x = 10
y = 1
z = 5.5
res = (x > y) and (z == y) 
print(res)

x = 10
y = 1
z = 5.5
res = x > y or not z == y and y != y + z / x 
print(res)

#EXERCICIO
nota_a = 8.5
nota_b = 7.2
nota_c = 9.8

if (nota_a >= 7 and nota_b >= 7 and nota_c >= 7):
    print('Você foi APROVADO em todas as matérias e passou de ano escolar.')
else:
    print('Você REPROVOU e não passou de ano escolar!')