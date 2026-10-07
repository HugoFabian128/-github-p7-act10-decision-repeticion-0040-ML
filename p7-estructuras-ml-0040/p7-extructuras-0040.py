# Hugo Fabian NC = 0040
# EJERCICIOS DE PYTHON - W3SCHOOLS
# Ejemplos por tema (2 por cada caso)
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. PYTHON CONDITIONS (Condiciones de comparación)
# ------------------------------------------------------------------------------
print("=== 1. PYTHON CONDITIONS ===")

# Ejemplo 1: Comprobar si un número es mayor que otro
x = 15
y = 10
if x > y:
    print(f"Ejemplo 1: {x} es mayor que {y}")

# Ejemplo 2: Comprobar igualdad entre cadenas de texto
usuario_registrado = "admin"
usuario_ingresado = "admin"
if usuario_registrado == usuario_ingresado:
    print("Ejemplo 2: El nombre de usuario es correcto.")

print("\n" + "-"*40 + "\n")


# ------------------------------------------------------------------------------
# 2. PYTHON IF ... ELIF (Estructura condicional múltiple)
# ------------------------------------------------------------------------------
print("=== 2. PYTHON IF ... ELIF ===")

# Ejemplo 1: Clasificación de temperatura
temperatura = 22
if temperatura > 30:
    print("Ejemplo 1: Hace calor.")
elif temperatura > 20:
    print("Ejemplo 1: El clima está agradable.")
elif temperatura > 10:
    print("Ejemplo 1: Hace fresco.")

# Ejemplo 2: Evaluación de nota de un estudiante
nota = 85
if nota >= 90:
    print("Ejemplo 2: Excelente calificación.")
elif nota >= 80:
    print("Ejemplo 2: Buena calificación.")
elif nota >= 70:
    print("Ejemplo 2: Calificación regular.")

print("\n" + "-"*40 + "\n")


# ------------------------------------------------------------------------------
# 3. PYTHON IF ... ELSE (Estructura con alternativa final)
# ------------------------------------------------------------------------------
print("=== 3. PYTHON IF ... ELSE ===")

# Ejemplo 1: Comprobar si una persona es mayor de edad
edad = 17
if edad >= 18:
    print("Ejemplo 1: Acceso concedido (Mayor de edad).")
else:
    print("Ejemplo 1: Acceso denegado (Menor de edad).")

# Ejemplo 2: Determinar si un número es par o impar
numero = 7
if numero % 2 == 0:
    print(f"Ejemplo 2: El número {numero} es PAR.")
else:
    print(f"Ejemplo 2: El número {numero} es IMPAR.")

print("\n" + "-"*40 + "\n")


# ------------------------------------------------------------------------------
# 4. PYTHON FOR LOOPS (Bucles For)
# ------------------------------------------------------------------------------
print("=== 4. PYTHON FOR LOOPS ===")

# Ejemplo 1: Recorrer una lista de elementos
frutas = ["Manzana", "Plátano", "Naranja"]
print("Ejemplo 1: Lista de frutas:")
for fruta in frutas:
    print(f" - {fruta}")

# Ejemplo 2: Generar una secuencia numérica con un rango
print("\nEjemplo 2: Contar del 1 al 5 usando range():")
for i in range(1, 6):
    print(f" Número: {i}")

print("\n" + "-"*40 + "\n")


# ------------------------------------------------------------------------------
# 5. PYTHON WHILE LOOPS (Bucles While)
# ------------------------------------------------------------------------------
print("=== 5. PYTHON WHILE LOOPS ===")

# Ejemplo 1: Contador simple ascendente
contador = 1
print("Ejemplo 1: Contador con bucle while:")
while contador <= 3:
    print(f" Valor actual: {contador}")
    contador += 1

# Ejemplo 2: Reducción de valor (cuenta regresiva)
fuerza = 100
print("\nEjemplo 2: Recibiendo daño en un juego:")
while fuerza > 60:
    print(f" Salud restada, salud actual: {fuerza}")
    fuerza -= 15

print("Hugo Fabian NC = 0040")