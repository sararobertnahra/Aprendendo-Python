restodadivisao = 28 % 3
print(restodadivisao)


numero = 4 + 6 * 7 - 5 / 5
print(numero)

quadrado = 3 ** 2
cubo = 7 ** 3
print(quadrado, cubo)

repetindopalavras = "Sara" * 10
print(repetindopalavras)


lista = [1, 2, 3] 
print (lista*3)

x = object()
y = object()

# TODO: change this code
x_list = [x]*10
y_list = [y]*10
big_list = [x, y]*10

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")