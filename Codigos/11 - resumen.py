#Creación de Cuentas
# -> nombre_cliente
# -> num_cuenta
# -> saldo_inicial
# -> tipo_de_cuenta
    #ahorro
    #monetaria

#Operaciones del cajera automatico
#Solicitud de salo
#Realizar transacciones
    #Realizar transacciones a terceros
    #Realizar transacciones a cuentas propias
#realizar Retiros
    #monetaria <= 5000
    #ahorro <= 2500
#realizar deposito
    #Depositos a terceros
    #Depositos a la cuenta logueada

#Manejo de Excepciones
#try - except 
# 'try' ':'
# '   ' bloque_código
# 'except' [clase] ':'
# '   ' bloque_código   

#Importaciones de librerias
# 'import' nombre_librería o paquete
# 'from' nombre_librería o paquete 'import' nombre_metodo o clase
from datetime import datetime

##------------------Estructuras y Variables Globales------------------##

#Estructuras
#() [] {} -> {}

##Cuentas por defecto 
    #1 de Ahorro
    #1 Monetaria
cuentas = {
    '2021-09-03Az': {
        'num_cuenta': '2021-09-03Al',
        'nombre': 'Alberto Lopez',
        'saldo': 5250,
        'tipo_cuenta': 1
    },
    '2021-09-03En': {
        'num_cuenta': '2021-09-03En',
        'nombre': 'Esteban',
        'saldo': 13250,
        'tipo_cuenta': 2
    }
}

#Ejemplo de diccionario
# dict1 = {
#     'llave1': {
#         'nombre': "Elian"
#     },
#     'llave2': {
#         'nombre': "Adolfo"
#     }
# }

# print(dict1)
# print(dict1['llave1'])
# print(dict1['llave2'])
# print(dict1['llave1']['nombre'])    #Elian
# print(dict1['llave2']['nombre'])    #Adolfo

# Variables globales

nombre_cliente = ""
saldo_inicial = 0
flag = True



#Inicio del Programa

print("Bienvenido al Banco Patitaspaquelasquier, S.A.");

while (True):
    
    print("\nMENÚ PRINCIPAL\n\n1. Crear Cuenta\n2. Cajero Automático\n3. Salir")
    
    try:
        opcion_principal = int(input("\nEscoja una opción: "))
    except:
        print(f"\nLa opción no es un número")
        continue

    if (opcion_principal == 1):
        print("\nCreación de Cuentas")

        while (True):
                
            print("\nTIPOS DE CUENTA\n\n1. Monetaria\n2. Ahorro\n3. Volver al menu principal")
            try:
                tipo_cuenta = int(input("\nIngrese el tipo de cuenta a crear: "))
            except:
                print(f"\nLa opción no es un número")
                continue

            if (tipo_cuenta == 1):
                nombre_cliente = input("\nPor favor, ingrese su nombre: ")

                while(True):
                    try:
                        saldo_inicial = float(input(f"\n{nombre_cliente} por favor, ingrese su saldo inicial: "))
                    except:
                        print(f"\nEl Saldo debé ser un número")
                        continue

                    if (saldo_inicial < 100):
                        print(f"\n{nombre_cliente} el saldo ingresado no es valido, deber ser mayor o igual a $100.00")
                        continue

                    num_cuenta = str(datetime.now()).split(' ')[0] + str(nombre_cliente[0]) + str(nombre_cliente[-1])

                    cuentas[num_cuenta] = {'num_cuenta': num_cuenta, 'nombre': nombre_cliente, 'saldo': saldo_inicial, 'tipo_cuenta': 1}
                    break

            elif (tipo_cuenta == 2):
                nombre_cliente = input("\nPor favor, ingrese su nombre: ")

                while(True):
                    try:
                        saldo_inicial = float(input(f"\n{nombre_cliente} por favor, ingrese su saldo inicial"))
                    except:
                        print(f"\nEl Saldo debé ser un número")
                        continue

                    if (saldo_inicial < 50):
                        print(f"\n{nombre_cliente} el saldo ingresado no es valido, deber ser mayor o igual a $50.00")
                        continue

                    num_cuenta = str(datetime.now()).split(' ')[0] + str(nombre_cliente[0]) + str(nombre_cliente[-1])

                    cuentas[num_cuenta] = {'num_cuenta': num_cuenta, 'nombre': nombre_cliente, 'saldo': saldo_inicial, 'tipo_cuenta': 2}
                    break
        
            elif (tipo_cuenta == 3):
                break

            else:
                print(f"\nLa opción: {tipo_cuenta} no es valida. Por favor ingrese una opción entre [1-3]")

    elif (opcion_principal == 2):
        print("\nCajero Automático")
        
        contador = 0
        flag = True

        while (True and flag):
            num_cuenta = input("\nIngrese el número de cuenta por favor: ")

            if (cuentas.get(num_cuenta) == None):
                print(f"\nEl número de cuenta no existe: {num_cuenta}")
                contador += 1

                if (contador == 3):
                    break
                
                continue

            nombre = cuentas[num_cuenta]["nombre"]
            saldo_inicial = cuentas[num_cuenta]["saldo"]
            tipo_cuenta = cuentas[num_cuenta]['tipo_cuenta']

            print(f"\nBienvenido {nombre}")

            while(True):
                print("\nMenu Cajero Automático\n")
                print("1. Consultar Saldo\n2. Trasnferencias\n3. Retiros\n4. Depositos\n5. Volver al menu principal")
                try:
                    opcion_cajero = int(input("\nPor favor seleccione una opción: "))
                except:
                    print("\nLo opción no es un número.")
                    continue

                if (opcion_cajero == 1):
                    print("\nCONSULTA DE SALDO")
                    print(f"{nombre} su saldo actual es de: ${saldo_inicial}\n")

                elif (opcion_cajero == 2):
                    pass
                    #aqui es donde deben programar lo que se pide

                elif (opcion_cajero == 3):
                    print("\nRETIRO DE DINERO")
                    
                    flag_retiro = True

                    while(flag_retiro):
                        try:
                            monto_retiro = float(input(f"{nombre}, ingrese el monto a retirar: "))
                        except:
                            print(f"\nEl monto a retirar debé ser un número")
                            continue

                        if (tipo_cuenta == 1):
                            if (monto_retiro <= 5000):
                                if (monto_retiro <= saldo_inicial):
                                    cuentas[num_cuenta]['saldo'] -= monto_retiro
                                    saldo_inicial -= monto_retiro
                                
                                else:
                                    print(f"\nNo dispone de saldo suficiente para realizar el retiro por: {monto_retiro}")

                            else:
                                print("\nEl tipo de cuenta Monetaria solo puede retirar un valor entre 1 y 5000 dólares")

                        else:
                            if (monto_retiro <= 2500):
                                if (monto_retiro <= saldo_inicial):
                                    cuentas[num_cuenta]['saldo'] -= monto_retiro
                                    saldo_inicial -= monto_retiro

                                else:
                                    print(f"\nNo dispone de saldo suficiente para realizar el retiro por: {monto_retiro}")

                            else:
                                print("\nEl tipo de cuenta de Ahorro solo puede retirar un valor entre 1 y 2500 dólares")

                        retiro_nuevo = input(f"\n{nombre} desea realizar otro retiro? [s/n]: ").lower()

                        if (retiro_nuevo == 'n'):
                            print()
                            flag_retiro = False

                elif (opcion_cajero == 4):
                    pass

                elif (opcion_cajero == 5):
                    flag = False
                    break

                else: 
                    print(f"\nLa opción: {opcion_cajero} no es valida, por favor ingresar una opción del [1-5]")


    elif (opcion_principal == 3):
        print("\nVuelva pronto :)")
        break

    else:
        print(f"\nLa opción: {opcion_principal} no es valida. Por favor ingrese una opción entre [1-3]")
