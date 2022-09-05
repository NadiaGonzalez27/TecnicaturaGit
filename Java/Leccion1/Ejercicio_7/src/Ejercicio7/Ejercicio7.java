
package Ejercicio7;

import java.util.Scanner;

public class Ejercicio7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        //Una compañia de carros usados, paga a su personal de ventas un salario de $1000
        //mensuales mas una comision de $150 por cada carro vendido, mas el 5% del valor
        //de la venta por carro. Cada mes el capturista de la empresa ingresa en la computadora
        //los datos pertinentes
        //Hacer un programa que calcule e imprima el salario mensual de un vendedor dado.
        
        final int salario = 1000; 
        int comision = 150, venta; 
        float salarioMensual, ventaCarro, porcVenta, totalPrecio; 
        
        System.out.println("Digite la cantidad de carros vendidos: ");
        venta = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el valor del carro: ");
        ventaCarro = Float.parseFloat(entrada.nextLine()); 
        
        comision *= venta;
        totalPrecio = ventaCarro * venta; 
        porcVenta = totalPrecio * 0.05f;
        salarioMensual = salario + comision + porcVenta; 
        
        System.out.println("\n El salario mensual es: "+salarioMensual);
        
    }
}
