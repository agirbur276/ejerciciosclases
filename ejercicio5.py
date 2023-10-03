'''EJERCICIO 5:
Requerir al usuario que ingrese un día de la semana en minusculas e imprimir un
mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es
sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.'''


diasemana = input("Dime un día de la semana en minúsculas: ")
if diasemana == "lunes":
    print("Venga que se puede")
elif diasemana == "viernes":
    print("Hoy es el ultimo dia fiestuqui")
elif diasemana == "sabado" or diasemana == "domingo":
    print("Más fiesta")
else:
    print("Tu puedessss")