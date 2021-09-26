#fibonacci
# 1, 1, 2, 3, 5, 8, 13, 21, 34

def fibonacci(num_terminos):
    termin1 = 1
    termin2 = 1

    result = "1"
    count = 1

    if num_terminos == 1:
        return result
    if num_terminos == 2:
        return result + ", 1"

    result += ", 1"
    while (count <= num_terminos):
                                    #                        1  2 aux
        if count > 2:               # 1, 1, 2, 3, 5, 8, 13, 21, 34
            aux = termin1 + termin2
            termin1 = termin2
            termin2 = aux

            result += f", {str(aux)}"
        count += 1
    return result

def fibonacci2(num): # Aporte de Diego Ortiz
    arr = [1,1]
    if num==1:
        print('0')
    elif num==2:
        print(*arr)
    else:
        while(len(arr)<num):
            arr.append(0)
        if(num==0 or num==1):
            return 1
        else:
            for i in range(2,num):
                arr[i]=arr[i-1]+arr[i-2]
            print(str(arr).replace('[', '').replace(']', ''))


#### Solución de Diego Ortiz a Fibo_recursiva_lista_elementos
def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n


def fibonacci_recursiva(num_elemtos, lista = [1, 1]):
    sucesion = lista
    if (num_elemtos == 1):
        return 1, sucesion

    if (num_elemtos == 2):
        return 1, sucesion

    termin1 = fibonacci_recursiva(num_elemtos - 1, sucesion)
    termin2 = fibonacci_recursiva(num_elemtos - 2, sucesion)

    result_num = termin1[0] + termin2[0]
    if result_num not in sucesion:
        sucesion.append(result_num)
        
    return result_num, sucesion


if __name__ == '__main__':
    print(fibonacci(10))
    fibonacci2(10)
    print(str(fibonacci_recursiva(10)[1]).replace('[', '').replace(']', ''))

    #Solución Diego Ortiz
    for i in range(1, 11):
        if i == 10:
            print(rec_fib(i), end= '')
            continue
        print(rec_fib(i), end= ', ')
