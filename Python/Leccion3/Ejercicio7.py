#Ejercicio 7
# Dadas las horas trabajadas de 5 personas, y la tarifa de pago. Calcular el salario,
# y la sumatoria de todos los salario

i = 1
suma = 0
for i in range(5):
    tarifa = int(input("Ingrese el salario por hora: "))
    horas = int(input("Ingrese la cantidad de horas trabajadas: "))

    salario = horas * tarifa
    print(f'El salario es: {salario}')
    suma = suma + salario

print(f'La suma de los salarios es: {suma}')