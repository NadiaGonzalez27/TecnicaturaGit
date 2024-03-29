class Persona2:
    def __init__(self, nombre, apellido, edad):  # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Método Setter
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @property
    def apellido(self):
        # print('Estamos utilizando el método get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        # print('Estamos utilizando el método set')
        self._apellido = apellido

    @property
    def edad(self):
        # print('Estamos utilizando el método get')
        return self._edad

    @edad.setter
    def edad(self, edad):
        # print('Estamos utilizando el método set')
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__': #Comprobacion del metodo main
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.nombre)  # Llamamos al método getter
    persona1.nombre = 'Juan Pedro'  # llamamos al metodo setter
    print(persona1.nombre)  # Otra vez con el método getter
    print(persona1.mostrar_detalles())  # Llamamos el método mostrar_detalles
    # Atributo read-only(solo lectura) seria la edad porque no tiene el método set
    print(persona1.edad)

    # Tarea crear tres objetos mas, utilizando los métodos getter and setter
    # para modificar, y mostrar los cambios con el método mostrar_detalles

    # Objeto numero uno de la tarea
    persona2 = Persona2('Nadia', 'Gonzalez', 26)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Rocio'
    persona2.apellido = 'Singuri'
    persona2.edad = 25
    print(persona2.mostrar_detalles())

    # Objeto numero dos de la tarea
    persona3 = Persona2('Hector', 'Pardo', 27)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Ariel'
    persona3.apellido = 'Troncoso'
    persona3.edad = 28
    print(persona3.mostrar_detalles())

    # Objeto numero tres de la tarea
    persona4 = Persona2('Agustin', 'Gonzalez', 5)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Ramiro'
    persona4.apellido = 'Troncoso'
    persona4.edad = 6
    print(persona4.mostrar_detalles())

    print(__name__)
