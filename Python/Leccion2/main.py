# En esta clase veremos la sentencia if/else
'''
condicion = 10
if condicion == True:
    print('Condicion verdadera')
elif condicion == False:
    print('Condicion falsa')
else:
    print('Condicion sin especificar')
'''
'''
num = int(input("Digite un numero en el rango de 1 al 3: "))
numTexto = ""
if num == 1:
    numTexto = "Numero uno"
elif num == 2:
    numTexto = "Numero dos"
elif num == 3:
    numTexto = "Numero tres"
else:
    numTexto = "Has ingresado un numero fuera de rango"
print(f'El numero ingresado es: {num} - {numTexto}')
'''
condicion = False
'''if condicion:
    print("Condecion Verdadera")
else:
    print("Condicion Falsa")'''

print("Condicion Verdadera") if condicion else print("Condicion Falsa")

