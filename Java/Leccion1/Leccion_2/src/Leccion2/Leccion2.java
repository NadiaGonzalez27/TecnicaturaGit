package Leccion2;

import java.util.Scanner;

public class Leccion2 {

    public static void main(String[] args) {
        //var condicion = false;
        //if (condicion) {
        //    System.out.println("Condicion verdadera"); //condicion simple
        //} else {
        //    System.out.println("Condicion Falsa"); //condicion doble 
        //}
        
        //var numero = 5;
        //var numeroTexto = "Numero desconocido";
        //if (numero == 1) {
        //    numeroTexto = "Numero uno";
        //}
        //else if(numero ==2){
        //    numeroTexto = "Numero dos";
        //}
        //else if(numero == 3){
        //    numeroTexto = "Numero tres";
        //}
        //else if(numero == 4){
        //    numeroTexto = "Numero cuatro";
        //}
        //else {
        //    numeroTexto = "Numero no encontrado";
        //}
        //System.out.println("numeroTexto = " + numeroTexto);
        
        //Sentencia de control switch
        Scanner entrada = new Scanner(System.in);
        /*System.out.println("Digite un numero del 1 al 4: ");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTexto = "Valor desconocido";
        switch(numero){
            case 1:
                numeroTexto = "Numero uno";
                break;
            case 2:
                numeroTexto = "Numero dos";
                break;
            case 3:
                numeroTexto = "Numero tres";
                break;
            case 4:
                numeroTexto = "Numero cuatro";
                break;
            default:
                numeroTexto = "Caso no encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);*/
        
        
        //EJERCICIO 2
        
        float compra, descuento;
        
        System.out.println("Digite la cantidad a pagar: ");
        compra = Float.parseFloat(entrada.nextLine());
        
        if (compra > 100){
            descuento = compra -(compra * 0.20F) ;
             
            System.out.println("El precio final es = " + descuento);
        }
        else{
            System.out.println("El precio final es =" + compra);; 
        }
    }
}
