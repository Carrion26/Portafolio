#11 tabla de multiplicar

numero = int(input("Ingrese número entero: "))

print(f"tabla de multiplicar {numero}:")
for i in range (1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")