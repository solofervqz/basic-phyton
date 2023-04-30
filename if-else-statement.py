print("Hola, este programa usa tres if ... else")

numero = int(input("Ingrese un número entero: "))

if numero < 15:
    print("El numero que ingresaste es menor que 15")
elif numero == 15:
    print("El numero que ingresaste es 15")
else:
    print("El numero que ingresaste es mayor que 15")

print(" ")

print("Segundo if ... else")
par_impar = int(input("Ingrese otro número entero: "))

if par_impar % 2 == 0:
    print("El numero que ingresaste par")
else:
    print("El numero que ingresaste es impar")

print(" ")

print("Tercer if ... else")
otro_num = int(input("Ingrese un número, el que sea: "))

if otro_num>0:
    print("El numero que ingresaste es positivo")
elif otro_num == 0:
    print("El numero que ingresaste es igual a 0")
else:
    print("El numero que ingresaste negativo")