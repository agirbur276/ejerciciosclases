'''EJERCICIO 4:
Solicitar al usuario que ingrese tres numeros y mostrar cual es el mayor de los tres.'''

num1= int(input("Dime un número: "))
num2= int(input("Dime otro número: "))
num3= int(input("Dime otro número: "))
if num1 >= num2 and num1 >= num3:
    print("este es el mayor de los tres numero:", num1)
elif num2 >= num1 and num2 >= num3:
    print("este es el mayor de los tres numero:", num2)
else:
    print("este es el mayor de los tres numero:", num3)