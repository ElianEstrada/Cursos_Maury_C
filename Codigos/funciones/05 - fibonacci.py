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


def fibonacci_recursiva(num_elemtos):
    if (num_elemtos == 1):
        return 1

    if (num_elemtos == 2):
        return 1

    result_num = (fibonacci_recursiva(num_elemtos - 1) + fibonacci_recursiva(num_elemtos - 2))
    return result_num


if __name__ == '__main__':
    print(fibonacci(10))
    fibonacci2(10)
    print(fibonacci_recursiva(10))


