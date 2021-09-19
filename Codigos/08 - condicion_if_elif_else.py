# Sintaxis del if - elif - else

#Los corchetes ([]) indican opcionalidad

# 'if' '(' condicion ')' ':'
# '    ' bloque_codigo':'
# '    ' bloque_codigo] -> se
# ['elif' '(' condicion2 ')'  puede repetir n veces.
# ['else' ':'
# '    ' bloque_codigo]

#Identificar que un número x 
#es positivo, 0 o negativo

x = -10;

if (x > 0):
    print(f"{x} es positivo");
elif (x == 0):
    print(f"{x} es cero");
else:
    print(f"{x} es negativo");