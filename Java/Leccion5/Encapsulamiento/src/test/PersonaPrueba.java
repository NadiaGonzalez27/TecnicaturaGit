
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //Modificamos a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; //Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); //Error
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
        //y imprimir, luego modificar sus valores y volver a imprimir
        
        Persona persona2 = new Persona("Rocio", 75000, true);
        System.out.println("persona2 su nombre es: "+persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo: "+persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: "+persona2.isEliminado());
        
        //Modificamos 
        persona2.setNombre("Nadia");
        System.out.println("persona1 con su nombre modificado: "+persona2.getNombre());
        persona2.setSueldo(80000);
        System.out.println("persona2 el resultado para sueldo modificado: "+persona2.getSueldo());
        persona2.setEliminado(false);
        System.out.println("persona2 para obtener el booleano modificado: "+persona2.isEliminado());
        
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1: "+persona1.toString());
    }
}
