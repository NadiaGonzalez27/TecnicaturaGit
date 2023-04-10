
package ar.com.codesystem.ventas;

public class Producto {
    //Atributos de la clase
    private int idPrducto;
    private String nombre;
    private double precio;
    private static int contadorProductos;
    
    //Constructor vacio
    private Producto(){
        this.idPrducto = ++Producto.contadorProductos;
    }
    
    public Producto(String nombre, double precio){
        this(); //Llamamos al constructor vacio para el aumento de idProducto
        this.nombre = nombre;
        this.precio = precio;
    }

    public int getIdPrducto() {
        return idPrducto;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    @Override
    public String toString() {
        return "Producto{" + "idPrducto=" + idPrducto + ", nombre=" + nombre + ", precio=" + precio + '}';
    }
}
