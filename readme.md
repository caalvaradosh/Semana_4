# Taller Semana 4 - Organización Modular de un Proyecto Python

## Estudiante

Clide Alvarado

## Descripción del sistema

Este proyecto consiste en un sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO).

El sistema permite:

* Registrar productos del restaurante.
* Registrar clientes.
* Gestionar la información mediante una clase principal llamada Restaurante.
* Mostrar los datos almacenados en consola.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   └── restaurante.py
└── main.py
```

### Modelos

Contienen las clases que representan las entidades principales del sistema:

* Producto
* Cliente

### Servicios

Contiene la clase Restaurante, encargada de administrar productos y clientes.

### Main

Archivo principal donde se crean los objetos y se ejecuta el programa.

## Tecnologías utilizadas

* Python 3
* Programación Orientada a Objetos

## Reflexión

La modularización permite organizar mejor el código, facilitando su mantenimiento, reutilización y comprensión. Separar responsabilidades entre modelos, servicios y el archivo principal ayuda a desarrollar programas más ordenados y escalables.
