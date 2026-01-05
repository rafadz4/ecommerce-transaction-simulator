# Ecommerce Transaction Simulator
Aplicación de consola desarrollada en Python que simula transacciones de un comercio electrónico mediante un sistema de carrito de compras.
El proyecto se enfoca en lógica backend, validación de entradas, diseño limpio de funciones y generación de datos estructurados para un posible análisis posterior.

##  Contexto/Introducción
Este proyecto simula el backend de una tienda virtual a través de una aplicación CLI (Command Line Interface). Los usuarios pueden interactuar con un catálogo de productos, gestionar un carrito de compras y finalizar pedidos. El sistema replica la lógica básica de un ecommerce real, con énfasis en: modularización del código , validación de entradas del usuario , manejo de errores ,diseño limpio y reutilizable de funciones . No cuenta con interfaz gráfica ni consumo de APIs externas. Toda la interacción se realiza mediante consola y estructuras de datos en memoria.

## Objetivo del proyecto 
- Simular transacciones de un comercio electrónico.
- Practicar lógica backend con Python.
- Generar datos estructurados de compras.
- Servir como base para análisis de datos posteriores.

## ✅ Requerimientos Funcionales
El sistema debe permitir al usuario interactuar a través del input de consola y realizar las siguientes acciones:

### 🧾 Catálogo
- Mostrar una lista de productos con sus nombres, códigos y precios.

Los productos están precargados al iniciar el programa.

### 🛒 Carrito de compras
- Agregar un producto al carrito a partir de su código.

- Validar si el código existe en el catálogo.

- Permitir agregar múltiples cantidades.

- Eliminar un producto del carrito.

- Vaciar el carrito completamente.

- Mostrar el contenido actual del carrito, con cantidades, precios individuales y total acumulado.

### 💳 Checkout
- Permitir al usuario finalizar la compra.

- Validar si hay productos en el carrito.

- Mostrar resumen de compra: productos, cantidades, total.

- Simular "procesamiento del pago" (print).

- Vaciar el carrito.

## 🔁 Loop de ejecución
El sistema debe ejecutarse en bucle hasta que el usuario decida salir.

Las acciones se muestran como un menú numérico:


```
1. Ver catálogo
2. Agregar producto al carrito
3. Eliminar producto del carrito
4. Vaciar carrito
5. Mostrar carrito
6. Finalizar compra
7. Salir
```

## 🎯 Registro de Datos (Opcional)
Agrega la funcionalidad de guardar un historial de compras en un archivo .txt o .csv, donde cada compra (al finalizar el checkout) se registre con:

- Fecha y hora (datetime)

- Lista de productos comprados

- Total de la compra

El archivo se actualiza sin sobrescribir registros anteriores, lo que permite su uso posterior para:

- análisis de ventas

- cálculo del ticket promedio

- identificación de productos más vendidos

- análisis temporal de ingresos

## 🧠 Buenas prácticas y sugerencias técnicas
- Usa typing para anotar tus funciones (por ejemplo, -> dict, -> list[str], etc.).

- Usa try/except para capturar errores de input del usuario (e.g., escribir texto cuando se espera un número).

- Usa estructuras como list, dict, set de forma adecuada:

  - dict para el catálogo ({codigo: {nombre, precio}})

  - dict o list para el carrito ({codigo: cantidad} o lista de tuplas)

- Modulariza tu código: crea funciones puras y separa la lógica del menú, la lógica de validación, etc.

- Agrega validaciones robustas (código inexistente, cantidades inválidas, carrito vacío en checkout).

- Usa os.system("clear") si quieres limpiar la consola en cada vuelta del menú (solo para Unix/Linux).

### 🧾 Ejemplo de Entrada/Salida

```
Bienvenido a la tienda virtual 🛍️
¿Qué deseas hacer?

1. Ver catálogo
2. Agregar producto al carrito
3. Eliminar producto del carrito
4. Vaciar carrito
5. Mostrar carrito
6. Finalizar compra
7. Salir
> 1

Código: A001 | Producto: Pan | Precio: S/1.50
Código: B203 | Producto: Leche | Precio: S/3.80
...

> 2
Ingrese código de producto: B203
Cantidad: 2
✔ Producto agregado al carrito.

> 5
Tu carrito:
- Leche (x2) -> S/7.60
Total: S/7.60

> 6
Resumen de compra:
Leche (x2) -> S/7.60
Total a pagar: S/7.60
Gracias por tu compra 🧾

> 7
Hasta pronto 👋
```
