# Sintaxis del if - elif

#Los corchetes ([]) indican opcionalidad

# 'if' '(' condicion ')' ':'
# '    ' bloque_codigo
# ['elif' '(' condicion2 ')' ':'
# '    ' bloque_codigo] -> se puede repetir n veces.

#Identificar si un número x 
#es positivo o 0

x = -2;

# if (x > 0):
#     print(f"{x} es positivo");
# elif (x == 0):
#     print(f"{x} es 0");
# else:
#     if (x == 0):
#         print(f"{x} es 0");  
# 

#Identificar si un número x 
# es postivo o 0 o -1  

if (x > 0):
    print(f"{x} es positivo");
elif (x == 0):
    print(f"{x} es 0");
elif (x == -1):
    print(f"{x} es -1");