#Sintaxis del for
# for in range

# 'for' contador 'in' 'range' '(' [numero| expresión aritmetica| un rango (1, 4)] ')' ':'
# '    ' bloque_codigo
#  

for _ in range(1, 11):
     print("Hola")

letter = 10
for letter in (1, 2, 3, 4):
    print(letter)

character = 'a'

string = ['H', 'o', 'l', 'a']

#print(*string)
word = "Hola"
print(word[0])
print(string[0])

contador = 0
while (contador < len(string)):
    print(string[contador])
    contador += 1