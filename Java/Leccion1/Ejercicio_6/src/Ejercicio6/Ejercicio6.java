
package Ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
       // Guillermo tiene N dolares. Luis tiene la mitad de lo que
       // posee Guillermo. Juan tiene la mitad de lo que 
       //posee Guillermo y Luis juntos. Hacer un programa que calcule e
       //imprima la cantidad de dinero que tienen entre los tres
        
        float Guillermo, Luis, Juan, total;
        System.out.println("Digite la cantidad de dinero que tiene Guillermo: ");
        Guillermo = Float.parseFloat(entrada.nextLine());
        
        Luis = Guillermo / 2; 
        Juan = (Guillermo + Luis)/ 2; 
        total = Guillermo + Luis + Juan;
        System.out.println("\n El dinero que tiene Luis es: U$$"+Luis);
        System.out.println("\n El dinero que tiene Juan es: U$$"+Juan);
        System.out.println("\n El total del dinero entre los 3 es: U$$"+total);
    }
}
