def suma (x, y):
    total = x+y
    return "El resultado de la suma de los dos numeros es " + str(total)

def resta (x, y):
    total = x-y
    return "El resultado de restar los dos numeros es " + str(total)

def multiplicación (x, y):
    total = x*y
    return "El resultado de restar los dos numeros es " + str(total)


num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))

print(suma (num1, num2))
print(resta (num1, num2))
print(multiplicación (num1, num2))
