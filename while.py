print("Primer while: Imprimir numeros del 1 al 15")
i=1
while i<=15:
    print("Número ", i)
    i += 1

print(" ")
print("Segundo while: Sumar numeros del 1 al 50")
i=1
total = 0
while i<=50:
    total += i
    i += 1
print("Total: ", total)

print(" ")
print("Tercer while: Imprimir los primeros 5 numeros pares")
i = 0
j = 1
while i<5:
    if j % 2 == 0:
        print(j)
        j += 1
        i += 1
    else:
        j += 1
