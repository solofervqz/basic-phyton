print("Este programa tiene tres operadores ternarios")

numero = float(input("1°. Introduce un número: "))

es_positivo = True if numero > 0 else False
print("El número es positivo:", es_positivo)

print(" ")
print("2°")
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

respuesta = num1 if num1 > num2 else num2
print("El número mayor es:", respuesta)

print(" ")
print("3°")
num = int(input("Introduce un número: "))

respuesta = "par" if num % 2 == 0 else "impar"
print("El número es:", respuesta)