//Ejercicio 1: Calcular estacion del año
let mes = "9";
let estacion; //Undefined
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Vaor incorrecto";
}
console.log("El valor corresponde a la estacion de: "+estacion);

//Ejercicio2: Hora del dia
let horaDia = 6;
let hora;
if(hora == 7 || hora == 8 ){ //if(horaDia >= 7 && horaDia <= 8)
    hora = "Desayunando";
}
else if(horaDia == 9 || horaDia == 10 || horaDia == 11 || horaDia == 12){//if(horaDia >= 9 && horaDia <= 12)
    hora = "Trabajando";
}
else if(horaDia == 13 || horaDia == 14){//if(horaDia >= 13 && horaDia <= 14)
    hora = "Almorzando";
}
else if(horaDia == 15 ){
    hora = " En un break";
}
else if(horaDia == 16 || horaDia == 17 || horaDia == 18 || horaDia == 19 || horaDia == 20){//if(horaDia >= 16 && horaDia <= 20)
    hora = "Trabajando";
}
else if(horaDia == 21 || horaDia == 22){//if(horaDia >= 21 && horaDia <= 22)
    hora = "Cenando";
}
else if(horaDia == 23 || horaDia == 24 || horaDia == 1 || horaDia == 2 || horaDia == 3 || horaDia == 4 || horaDia == 5 || horaDia == 6){//if(horaDia >= 23 && horaDia <= 6)
    hora = "Durmiendo";
}
else{
    hora = "Hora no encontrada";
}
console.log("Segun la hora del día estoy: "+hora);

//Estructura switch(la sintaxis es igual a Java)
switch(mes){ //No solo se pueden utilizar numero, tambien cadenas
    case 1: case 2: case 12:
    estacion = "Verano";
    break;
    case 3: case 4: case 5:
    estacion = "Otoño";
    break;
    case 6: case 7: case 8:
    estacion = "Invierno";
    break;
    case 9: case 10: case 11:
    estacion = "Primavera";
    break;
    default:
        estacion = "Valor incorrecto";
}
console.log("Bienvenidos a la estación de: "+estacion);

//Ampliaremos el uso de var let y const
/*
Con var puedes reasignar en cualquier momento 
esta forma parte del ambito global
Un error es que se sobreescriba
*/

var nombre = 'Ariel';
nombre = 'Osvaldo';
console.log(nombre);

function saludar(){
    var nombre = 'Natalia';
    console.log(nombre);
}
console.log(nombre); //Aqui no lee el dato en la funcion


if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); //En la funcion funciono correctamente, en la estructura if fallo

/*
let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/ 

function saludar2(){
    let nombre2 = 'Ariel';
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2);

/*
const se utiliza para valores constantes que no pueden ser reasignados
*/ 

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //solo se ejecuta el console anterior
