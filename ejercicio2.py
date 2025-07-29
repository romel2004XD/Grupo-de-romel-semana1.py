# Ejercicio 2 – Conversión de tipos

# Paso 1: Solicitar al usuario su edad
# La función input() siempre devuelve un dato tipo cadena (str)
edad_str = input("Por favor, ingresa tu edad: ")

# Paso 2: Convertir la edad a un número entero (int)
edad = int(edad_str)

# Paso 3: Multiplicar la edad por 2
edad_doble = edad * 2

# Paso 4: Mostrar el resultado en pantalla
print("El doble de tu edad es:", edad_doble)