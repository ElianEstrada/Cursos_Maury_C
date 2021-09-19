#declarar una lista

lista_ejemplo = [] #esta es una lista vacía.

lista_ejemplo_datos = [1, "Hola", True, 1.2]

# print(lista_ejemplo)
# print(lista_ejemplo_datos)

#operaciones a listas

#añadir
#eliminar
#recorrer
#ordenar
#visualizar

#operacion - añadir

print(lista_ejemplo)
lista_ejemplo.append(1)
print(lista_ejemplo)
lista_ejemplo.append(2)
print(lista_ejemplo)
lista_ejemplo.append(3)
lista_ejemplo.append(4)
lista_ejemplo.append(5)
print(lista_ejemplo)

                  # 0  1  2  3  4
# lista_ejemplo -> [1, 2, 3, 4, 5]

print(lista_ejemplo[2])
print(lista_ejemplo[4])

#saber el tamaño de una lista
#len()

print(len(lista_ejemplo))

lista_ejemplo[len(lista_ejemplo) - 1]

#insert

lista_ejemplo.insert(0, 0)
print(lista_ejemplo)
# lista_ejemplo = [0, 1, 2, 3, 4, 5]
lista_ejemplo.insert(1, 0.5)
print(lista_ejemplo)
# lista_ejemplo = [0, 0.5, 1, 2, 3, 4, 5]
lista_ejemplo.insert(3, 1.5)
print(lista_ejemplo)
# lista_ejemplo = [0, 0.5, 1, 1.5, 2, 3, 4, 5]
lista_ejemplo.insert(5, 2.5)
print(lista_ejemplo)
# lista_ejemplo = [0, 0.5, 1, 1.5, 2, 2.5, 3, 4, 5]
lista_ejemplo.insert(7, 3.5)
# lista_ejemplo = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5]
lista_ejemplo.insert(9, 4.5)
print(lista_ejemplo)

#recorrer

for item in lista_ejemplo:
    print(item)

contador = 0
while (contador < len(lista_ejemplo)):
    print(lista_ejemplo[contador])

    contador += 1

#dada una lista devolver una lista con sus cuadrados
#lista original -> 1, 2, 3, 4, 5
#lista devuelta -> 1, 4, 5, 16, 25

lista_origen = [1, 2, 3, 4, 5]
lista_esperada = []

for item in lista_origen:
    lista_esperada.append(item**2)

print(lista_esperada) # -> 1, 4, 9, 16, 25


#remove

print(lista_ejemplo)
lista_ejemplo.remove(5)
print(lista_ejemplo)
lista_ejemplo.remove(3)
print(lista_ejemplo)

ultimo_elemento = lista_ejemplo.pop()
print(lista_ejemplo)
print(ultimo_elemento)
ultimo_elemento = lista_ejemplo.pop(3)
print(lista_ejemplo)
print(ultimo_elemento)


lista_desordenada = [4, 3, 2, 5, 12, 14, 8, 0, 1]
print(lista_desordenada)
lista_desordenada.sort()
print(lista_desordenada)
lista_desordenada.sort(reverse=True)
print(lista_desordenada)