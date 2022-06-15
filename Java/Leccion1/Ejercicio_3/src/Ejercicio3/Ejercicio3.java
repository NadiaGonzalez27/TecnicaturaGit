
package Ejercicio3;

import java.util.Scanner;


public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        //Sacar área y perímetro de un rectángulo
        float area, perimetro, largo, ancho;
  
        System.out.println("Digite el largo de un rectangulo: ");
        largo = Float.parseFloat(entrada.nextLine());
        
        System.out.println("Digite el ancho de un rectangulo: ");
        ancho = Float.parseFloat(entrada.nextLine());
       
        area = largo*2 + ancho *2 ;  
        perimetro = largo * ancho; 
        
        System.out.println("\n El area de un rectangulo es: "+ area);
        System.out.println("\n El perimetro de un rectangulo es: "+perimetro);
        
                
    }
 
}
