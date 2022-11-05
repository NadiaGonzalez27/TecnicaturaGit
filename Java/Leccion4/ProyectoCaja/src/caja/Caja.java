/*
Proyecto caja:
Ejercicio 1: Crear un proyecto segun las especificasciones
mostradas a continuacion.
La formula es: volumen = ancho * alto * profundidad
 */
package caja; //Package

public class Caja { //Calse publica caja
    //Atributos (caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //Metodo y constructores(acciones)
    public Caja(){ //Constructor 1 = vacio
    }
    //Constructor con parametros
    public Caja(int ancho, int alto, int profundo){ //Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen(){ //Metodo para calcular
        return ancho * alto * profundo;
    }
}
