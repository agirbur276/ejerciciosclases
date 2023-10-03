'''EJERCICIO 2:
Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. No
considerar el caso en que ambos números son iguales.'''

num1= int(input("Dime un número: "))
num2= int(input("Dime otro número: "))
if num1 < num2:
    print(num1,"es menor que",num2)
else:
    print(num2,"es menor que", num1)
                
    