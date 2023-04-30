#show you how to specify the default values for function parameters

def saludo (nombre = "Carlo", edad = 25):
    print(f"Hola {nombre}, tienes {edad} años")

def rectangulo (base = 2, altura = 2):
    area = base*altura
    print(f"La base es {base}, la altura es de {altura}. El area total es de {area}")

def divisible (numero, divisor = 2):
    if numero % divisor == 0:
        print("El número que introduciste SI es divisible entre 2")
    else:
        print("El número que introduciste NO es divisible entre 2")
        

print("Esta es la primera funcion: ")
saludo()
name = input("Ingresa tu nombre: ")
age = input("Ingresa tu edad: ")
saludo(name, age)

print(" ")
print("Esta es la segunda funcion")
rectangulo()
lado1 = int(input("Ingresa la base del rectángunlo: "))
lado2 = int(input("Ingresa la altura del rectángulo: "))
rectangulo(lado1, lado2)

print(" ")
print("Esta es la tercera funcion")
num = int(input("Ingresa un numero entero positivo: "))
divisible(num)
