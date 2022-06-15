
package Ejercicio4;

import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        //El mayor de dos números (Operador Ternario)
        int num1, num2;  
        System.out.println("Digite num1: ");
        num1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite num2: ");
        num2 = Integer.parseInt(entrada.nextLine());
        System.out.println((num1 > num2)? "El mayor es\n num1":"El mayor es\n num2");
        
        
       
        
        
    }
}
