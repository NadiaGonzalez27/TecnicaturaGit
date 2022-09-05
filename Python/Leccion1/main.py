'''
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escriben x624, la variable y = x368, la variable z = x688
print(id(y))
print(id(z))

# Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (String)
miGrupoFavorito = "La konga"
caracteristicas = "Banda XXI"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)

# numero1 = "7"
# numero2 = "8"
# print(int(numero1) + int(numero2))

# Tipos Booleanos (Bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# funcion input
# resultado = input("Digite un numero: ")  # regresa un dato tipo string
# print(resultado)

# Conversion de la entrada de datos (funcion input)
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
'''
"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("Resultado de la suma es:", suma)
print(f'El resultadp de la suma es: {suma}')

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")

modulo = operandoA % operandoB
print(f"El resultado de la division o residuo (modulo) es: {modulo}")

exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")
"""
""""
alto = int(input("Proporciona el alto del rectangulo: "))
ancho = int(input("Proporciona el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('Area: ', area)
print('Perimetro: ', perimetro
"""
"""
# Operadores Logicos
a = False
b = False
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)
"""

"""
# Ejercicio: Valor dentro de un rango
valor = int(input("Digite un numero: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f'El valor {valor} esta dentro del rango')
else:
    print(f'El valor {valor} No esta dentro del rango')
"""
"""
# Ejercicio: Operador or. Operador not
vacaciones = True
diaDescanso = True
if not (vacaciones or diaDescanso):
    print("Tiene trabajo que hacer")
else:
    print("Puede asistir al juegor")
"""
"""
# Ejercicio: Rango entre las edades 20 y 30 años
edad = int(input("Digite su edad: "))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    if veinte:
        print("Estas dentro del rango de los (20\'0) años")
    elif treinta:
        print("Estas dentro del rango de los (30\'0) años")
    else:
        print("No estas dentro del rango")
else:
    print("No estas dentro del rango de los (20\'0) a (30\'0) años")
"""
"""
# Ejercicio: El mayor de dos numeros
numero1 = int(input("Digute el valor para el numero1: "))
numero2 = int(input("Digite el valor para el numero2: "))

if numero1 > numero2:
    print("El numero 1 es mayor")
else:
    print("El numero 2 es mayor")
"""

# Ejercicio: Tienda de libros
print("Digite los siguientes datos del libro")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el Id del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar si el envio es gratuito (True/False): ")
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto, debe escribir True/False"
print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio: {precio}
    Envio Gratuito?: {envioGratuito}
''')









