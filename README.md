# poo_python
- el paradigma de POO esta basado en una abtracion del mundo real que nos va a permitir desarrollar programas de forma mas cercana a como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos.

## clase

- una clase es un tipo de dato cullas variables se llaman objetos o instancias.
- la clase es la definicion del concepto del mundo real y los objetos o instancias son el propio objeto del mundo real
- las clases estan compuestas por 2 elemetos: atributos y metodos.

### atributos
- los atributos son informacion que alamsena la clase

### metodos
- son las operaciones que pueden realisar las clases

## definicion de una clase en python

```Python
class Nombreclase:
    def _init_(self, variable1, variable2):
        self.Atributo1 = valor1
        self.Atributo2 = valor2

    def nombreMetodo(self):
    bloqueCodigo
```

### componentes

```class```: palabra reservada en Python para definir una clase.

```Nombreclase```: nombre de la clase que quieres crear

```def```: palabra reservada en Python que se utiliza para definir tanto el constructor de la clase (metodo que se ejecuta la primera vez que usas una clase) comolos diferentes metodos que tiene.

```_init_```: palabra reservada en python para definir el constructorde la clase. es lo primero que se ejecuta cuando creas un objeto de una clase

```(self, variablex)```: parametro del constructor de la clase. el parametro self es obligatorio y despues puedes tener tantos parametros como quieras. la forma de añadir parametros es la misma que las funciones.

```self.Atributox```: forma de utilizacion y acceso a los atributos de la clase.

```nombreMetodo```: nombre del metodo de la clase

```(self)```: parametros del metodo. el parametro self es obligatorio y despues puedes tener tantos parametros como quieras.

```bloqueCodigo```: instrucciones que ejecutara el metodo.

- cuando defines una clase deves tener en cuenta los suguientes puntos:
     - puedes definir tantos atributos como necesites.
     - puedes definir tantos metodos como necesites
     - puedes definir tantos parametros en el constructor y en los metodos como necesites.
     
## composicion
- consiste en la creacion de nuevas clases apartir de nuevas clases ya existentes que actuan como elementos compositores de la nueva
- las clases existentes seran atributos de la nueva clase
- en POO la composicion significa que entre las 2 clases existe una relacion del tipo "tiene un"
- ejemplo:
    - una cordenada en 2 dimensiones esta compuesta por 2 valores, el valor en el eje de las x y el valor en el eje de las y, esto podria ser una clase. un cuadrado esta conpuesto por 4 cordenadas que son los 4 vertices, esto podria ser una clase que esta compuesta por 4 clases del objeto cordenada