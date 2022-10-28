class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular_area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben ser tres.
    """

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = int(input("Digite la base del Rectangulo1: "))
altura = int(input("Digite la altura del Rectangulo1: "))
rectangulo1 = Rectangulo(base,altura)
print(f'El area del rectangulo1 es: {rectangulo1.calcular_area()}')

base = int(input("Digite la base del Rectangulo2: "))
altura = int(input("Digite la altura del Rectangulo2: "))
rectangulo2 = Rectangulo(base, altura)
print(f'El area del rectangulo2 es: {rectangulo2.calcular_area()}')

base = int(input("Digite la base del Rectangulo3: "))
altura = int(input("Digite la altura del Rectangulo3: "))
rectangulo3 = Rectangulo(base, altura)
print(f'El area del rectangulo3 es: {rectangulo3.calcular_area()}')
