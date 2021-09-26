# Factorial de un número 
# 5! = 5*4*3*2*1
# 4! = 4*3*2*1
# 3! = 3*2*1

#Función recusiva para el factorial de un número

def factorial(n):
    if (n == 0):    #
        return 1    # Caso base

    return n * factorial(n - 1)  #Aplicación


def main():
    print(factorial(7))

if __name__ == '__main__':

    main()