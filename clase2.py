#Ejercicio 1
# numero = int(input("ingrese un numero"))
# if(numero < 19):
#     print("el numero es menor que 19")

# print("fin del algoritmo")

# numero = int(input("ingrese un numero"))
# if(numero < 19):
#     print("el numero es menor que 19")
# else:
#     print("el numero es mayor que 19")

# print("fin del algoritmo")

#Ejercicio 2
# numero = int(input("ingrese un numero"))

# if(numero > 0):
#     print("el numero es positivo")

# else:
#     if(numero < 0):
#         print("el numero es negativo")
#     else:
#         print("el numero es neutro")

# print("fin del algoritmo")

#Ejercicio 3
# numero = int(input("ingrese un numero"))

# if(numero % 2 == 0):
#     print("el numero es par")

# else:
#     print("el numero es impar")

# print("fin del algoritmo")

#Ejercicio 4
# nota_final = float(input("ingrese la suma de todas las notas que se saco x alumno"))

# if(nota_final >= 6):
#     print("el alumno esta aprobado")

# else:
#     print("el alumno esta desaprobado")

# print("fin del algoritmo")

#Ejercicio 5
# año_nacimiento = int(input("ingrese el año de nacimiento"))
# año_actual = int(input("ingrese el año actual"))
# edad_minima = int(input("ingrese la edad minima del puesto"))

# if(edad_minima >= 18):
#     print("la edad minima es 18")

# edad_postulantes = año_nacimiento - año_actual

# if(edad_postulantes):
#     print("el postulante tendra la edad necesaria para llenar la vacante")

# else:
#     print("el postulante NO tendra la edad necesaria para llenar la vacante")

# print("fin del algoritmo")

#Ejrcicio 6
# numero1 = int(input("ingrese un numero"))
# numero2 = int(input("ingrese un numero"))

# if(numero1 == numero2):
#     print("son iguales")

# elif(numero1 > numero2):
#     print("el numero1 es el mayor")
# else:
#     print("el numero2 es el mayor")

# print("fin del algoritmo")

#Ejercicio 7
# tarjeta = input("ingrese el nombre de la tarjeta")

# if(tarjeta == "visa"):
#     print("tarjeta visa")

# else:
#     print("otra tarjeta")

# print("fin del algoritmo")

#Ejercicio 8
# monto = float(input("ingrese el monto "))
# tarjeta = input("ingrese tarjeta")
# # cuotas = int(input("ingrese el numero de cuotas"))

# # if(cuotas == 3):
# #     monto = monto * 1.03
# # elif(cuotas == 8):
# #     monto = monto * 1.17
# # elif(cuotas == 12):
# #     monto = monto * 1.32

# if(tarjeta == "visa"):
#     recargo_visa = monto * 1.07
#     print("monto total:", recargo_visa)
# elif(tarjeta == "mastercard"):
#     recargo_master = monto * 1.11
#     print("monto total:", recargo_master)
# else:
#     print("monto total", monto)

#Ejercicio 9


#Ejercicio 10
# numero = int(input("ingrese un numero"))

# if(numero % 2 == 0 or numero % 5 == 0):
#     print(numero ** 3)
# else:
#     print("no es multiplo de 2 ni de 5")

#Ejercicio 11

#Ejercicio 12
# mes = int(input("ingrese el numero del mes"))

# if(mes >= 1 and mes <= 12):
#     if(mes == 2):
#         print("el mes tiene 28")
#     elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
#         print("el mes tiene 30 dias")
#     else:
#         print("el mes tiene 31")
# else:
#     print("el numero del mes es incorrecto")

#Ejercicio 14
# dia = int(input("ingrese numero del dia"))
# mes = int(input("ingrese el numero del mes"))

# if(mes >= 1 and mes <= 12):
#     if(mes == 2):
#         print("el mes tiene 28")
#         if(dia >= 1 and dia <= 28):
#             print("fecha correcta")
#         else:
#             print("fecha incorrecta")
#     elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
#         print("el mes tiene 30 dias")
#     else:
#         print("el mes tiene 31")
# else:
#     print("el numero del mes es incorrecto")

#Ejercicio 15
# temperatura = float(input("ingrese el valor de temperatura"))
# escala = input("ingrese la escala C|F")

# if(escala == "C"):
#     print("la temperatura en grados farenheit es", (temperatura * 9/5) + 32)
# elif(escala == "F"):
#     print("la temperatura en grados celsius es", (temperatura - 32) * 5/9)
# else:
#     print("la escala ingresada es incorrecta")

#Ejercicio 16
# dia = int(input("ingrese numero del dia"))
# mes = int(input("ingrese el numero del mes"))
# año = int(input("ingrese el numero del año"))

# if(mes >= 1 and mes <= 12):
#     if(mes == 2):
#         if(dia >= 1 and dia <= 28):
#             if(dia == 28):
#                 dia = 1
#                 mes = mes + 1
#             else:
#                 dia = dia + 1
#     elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
#         if(dia == 30):
#             dia = 1
#             mes = mes + 1
#         else:
#             dia = dia + 1
#     else:
#         if(dia >= 1 and dia <= 31):
#             if(dia == 31):
#                 dia = 1
#                 mes = mes + 1
#             else:
#                 dia = dia + 1
#             if(mes == 13):
#                 mes = 1
#                 año = año + 1

#     print(dia, "/",mes, "/",año)
# else:
#     print("el numero del mes es incorrecto")

#Ejercicio 17

#Ejercicio 18
# num1 = int(input("ingrese valor de la carta 1"))
# palo1 = input("ingrese palo de la carta 1")
# num2 = int(input("ingrese valor de la carta 2"))
# palo2 = input("ingrese palo de la carta 2")
# num3 = int(input("ingrese valor de la carta 3"))
# palo3 = input("ingrese palo de la carta 3")

# if(palo1 == palo2 and palo1 == palo3):
#     puntos = 20
#     if(num1 <= 7):
#         puntos = puntos + num1
#     if(num2 <= 7):
#         puntos = puntos + num2
#     if(num3 <= 7):
#         puntos = puntos + num3
#     print("flor", puntos)
# elif(palo1 == palo2 or palo1 == palo3 or palo2 == palo3):
#     puntos = 20
#     if(palo1 == palo2):
#         if(num1 <= 7):
#             puntos = puntos + num1
#         if(num2 <= 7):
#             puntos = puntos + num2
#     elif(palo1 == palo3):
#         if(num1 <= 7):
#             puntos = puntos + num1
#         if(num3 <= 7):
#             puntos = puntos + num3
#     elif(palo2 == palo3):
#         if(num2 <= 7):
#             puntos = puntos + num2
#         if(num3 <= 7):
#             puntos = puntos + num3
#     print("envido", puntos)

#Ejercicio 20
# num1 = int(input("ingrese un numero"))
# num2 = int(input("ingrese un numero"))
# num3 = int(input("ingrese un numero"))
# num4 = int(input("ingrese un numero"))
# num5 = int(input("ingrese un numero"))

# cantidad_multiplos_3 = 0

# if(num1 % 3 == 0):
#     cantidad_multiplos_3 += 1

# if(num2 % 3 == 0):
#     cantidad_multiplos_3 += 1

# if(num3 % 3 == 0):
#     cantidad_multiplos_3 += 1

# if(num4 % 3 == 0):
#     cantidad_multiplos_3 += 1

# if(num5 % 3 == 0):
#     cantidad_multiplos_3 += 1

# print("cantidad de multiplos de 3", cantidad_multiplos_3)
