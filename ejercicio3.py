'''EJERCICIO 3:
Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor.
Considerar el caso en que ambos números son iguales.'''

num1= int(input("Dime un número: "))
num2= int(input("Dime otro número: "))
if num1 < num2:
    print(num1,"es menor que",num2)
elif num2<num1:
    print(num2,"es menor que", num1)
else:
    print("Ambos números son iguales.")

