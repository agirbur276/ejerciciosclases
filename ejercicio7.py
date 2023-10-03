'''EJERCICIO 7:
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
#ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte
#al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
#que tributar o no.'''


edad=int(input("Dime la edad:"))
ingresos=int(input("Dime tus ingresos:"))

def ejercicio7 (edad, ingresos):
    if (edad > 16 and ingresos > 1000):
        print("A pagar")
    else:
        print("No pagas")

ejercicio7(edad, ingresos)

