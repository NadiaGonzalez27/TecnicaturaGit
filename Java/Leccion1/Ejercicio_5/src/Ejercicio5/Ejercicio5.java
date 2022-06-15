
package Ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Hacer un programa que calcule e imprima la suma de tres calificaciones
        
        float nota1, nota2, nota3, suma;
        System.out.println("Digite las tres calificaciones: ");
        nota1 = Float.parseFloat(entrada.nextLine());
        nota2 = Float.parseFloat(entrada.nextLine());
        nota3 = Float.parseFloat(entrada.nextLine());
        
        suma = nota1 + nota2 + nota3;
        System.out.println("\n La suma de las calificaciones es: "+suma);
        
        
        
        
        
        
    }
}
