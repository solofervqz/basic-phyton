print("Primer for con range(): Imprimir numeros del 0 al 5")
for i in range(5):
    print("Iteración número", i)


print("Segundo for con range(): Imprimir numeros del 1 al 10")
for i in range(1, 11):
    print(i)

print("Tercer for con range(): Sumar los numeros del 1 al 50")
total = 0
for i in range(1, 51):
    total += i
print("El total es: ", total)