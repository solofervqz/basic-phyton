#learn how to use the keyword arguments to make the function call more obvious

def rectangulo(base, altura):
    return  base * altura

def crear_persona(nombre, edad, ciudad="Guadalajara"):
    persona = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
    return persona

def imprimir_lista_numeros(numeros, prefijo=""):
    for numero in numeros:
        print(f"{prefijo}{numero}")

print("Esta es la primera funcion: ")
area = rectangulo(base=5, altura=10)
print("El area del rectangulo de 5 por 10 es: ", area)

print("Esta es la segunda funcion: ")
persona = crear_persona(nombre="Fer", edad=21, ciudad="Chihuahua")
print("Se ha registrado una persona: ", persona)

print("Esta es la tercera funcion: ")
numeros = [4, 5, 6, 7 ,8 ]
print("imprime una lista de numeros del 4 al 8")
imprimir_lista_numeros(numeros, prefijo="Número: ")