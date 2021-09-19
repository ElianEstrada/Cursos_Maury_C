lista_des1 = [2, 4, 5, 1, 2, 0, 12, 13, 15]

#Algoritmos de Ordenamiento

# Burbuja (Bubblesort)

a = lista_des1
print(a)
i = 1
while (i < len(a)):
    j = 0
    while (j < len(a) - 1):

        if (a[j] > a[j + 1]):
            aux = a[j]
            a[j] = a[j + 1]
            a[j + 1] = aux

        j += 1
    i += 1

print(a)

#0  1  2  3  -> indices
#2, 4, 5, 1  -> valores

# i = 1
# j = 0
#primera iteración i 
    # primera iteración de j -> 0

    #lista_original = 
    #0  1  2  3  -> indices
    #2, 4, 5, 1  -> valores

    #a[0] -> 2
    #a[1] -> 4
    # a[0] > a[1] -> 2 > 4
    #j = j + 1

    # segunda iteración de j -> j = 1
    #lista_original = 
    #0  1  2  3  -> indices
    #2, 4, 5, 1  -> valores

    #a[1] -> 4
    #a[2] -> 5
    # a[1] > a[2] -> 4 > 5
    # j = 1 + 1

    # tercera iteración de j -> j = 2
    #lista_original = 
    #0  1  2  3  -> indices
    #2, 4, 5, 1  -> valores

    #a[2] -> 5
    #a[3] -> 1
    #a[2] > a[3] -> 5 > 1
        #aux = a[2] -> aux = 5
        #a[2] = a[3] -> a[2] = 1
        #a[3] = aux -> a[3] = 5

        #lista_semi_ordenada = 
        #0  1  2  3  -> indices
        #2, 4, 1, 5  -> valores
    
    #j = 2 + 1

# i = i + 1

# segunda iteración de i -> 2

    # j = 0
    # primera iteración de j -> 0
    #lista_original = 
    #0  1  2  3  -> indices
    #2, 4, 1, 5  -> valores

    #a[0] -> 2
    #a[1] -> 4
    # a[0] > a[1] -> 2 > 4
    # j = j + 1

    #segunda iteración de j -> 1
    #lista_original = 
    #0  1  2  3  -> indices
    #2, 4, 1, 5  -> valores

    #a[1] = 4
    #a[2] = 1
    # a[1] > a[2] -> 4 > 1
        #aux = a[1] -> aux = 4
        #a[1] = a[2] -> a[1] = 1
        #a[2] = aux -> a[2] = 4
        #lista_original = 
        #0  1  2  3  -> indices
        #2, 1, 4, 5  -> valores

    # j = j + 1

    #tercera iteración de j -> 2
    #lista_original = 
    #0  1  2  3  -> indices
    #2, 1, 4, 5  -> valores

    #a[2] -> 4
    #a[3] -> 5
    #a[2] > a[3] -> 4 > 5
    # j = j + 1

#i = i + 1

#tercerca iteración de i -> 3

    #j = 0
    #primera itereación de j -> 0
    #lista_original = 
    #0  1  2  3  -> indices
    #2, 1, 4, 5  -> valores

    #a[0] -> 2
    #a[1] -> 1
    #a[0] > a[1] -> 2 > 1
        #aux = a[0] -> aux = 2
        #a[0] = a[1] -> a[0] = 1
        #a[1] = aux -> a[1] = 2

        #lista semi_ordenada
        #0  1  2  3  -> indices
        #1, 2, 4, 5  -> valores

#1, 2, 4, 5
    