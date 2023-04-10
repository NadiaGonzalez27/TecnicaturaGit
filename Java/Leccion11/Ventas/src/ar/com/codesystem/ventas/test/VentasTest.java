
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3 = new Producto("Remera", 3500.00);
        Producto producto4 = new Producto("Zapatilla", 40500.00);
        Producto producto5 = new Producto("Bufanda", 2500.00);
        Producto producto6 = new Producto("Gorro", 1500.00);
        Producto producto7 = new Producto("Buzo", 13000.00);
        Producto producto8 = new Producto("Sweter", 18500.00);
        Producto producto9 = new Producto("Conjunto deportivo", 33300.00);
        Producto producto10 = new Producto("Sandalia", 22500.00);
        
        Orden orden1 = new Orden();
        //Agregamos productos a la lista
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.mostrarOrden();
        
        //Tarea:
       //Crear mas objetos de tipo Producto = 10
       //Crear mas objetos de tipo Orden = 2
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto10);
        orden2.agregarProducto(producto8);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto6);
        orden2.mostrarOrden();
        
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto2);
        orden3.agregarProducto(producto5);
        orden3.agregarProducto(producto7);
        orden3.mostrarOrden();
       
    }
}
