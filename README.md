# Complex Operations Library

## Descripción

Esta biblioteca proporciona funciones para realizar operaciones con números complejos. Incluye funciones para la suma, producto, resta, división, módulo, conjugado, conversión entre coordenadas cartesianas y polares, y cálculo de fase.

## Requisitos

Asegúrate de tener Python 3.11 instalado en tu sistema antes de utilizar esta biblioteca.

## Instalación

1. Descarga el código fuente desde el repositorio.
2. Abre una terminal y navega hasta el directorio del proyecto.


## Uso

Importa el módulo `operaciones` en tu script y utiliza las funciones proporcionadas:

```python
from operaciones import suma, Producto, resta, Division, Modulo, conjugado, polar_a_cartesiano, cartesiano_a_polar, fase

# Ejemplo de uso
a = (1, 1)
b = (5, -2)

print(conjugado(a))
print(cartesiano_a_polar(b))
