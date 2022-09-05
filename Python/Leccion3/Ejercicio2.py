# Ejercicio 2
# Calcular la suma de "N" primeros numeros
num = int(input("Ingrese la cantidad de numeros a sumar: "))
suma = 0
for i in range(num):
    suma = suma + i
print(f'La suma es: {suma}')