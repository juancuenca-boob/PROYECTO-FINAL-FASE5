# Universidad Nacional Abierta y a Distancia - UNAD
# Estudiante: (Juan Diego Sanchez Cuenca)
# Programa: Ingeniería en telecomunicaciones y redes
# Fundamentos de Programación - Código: 213022
# Fase 5 - Evaluación Final POA
# Problema 2: Gestión de precios del menú de restaurante

# --- Constantes de la promoción ---
CATEGORIA_OBJETIVO = "Bebidas"
UMBRAL_PRECIO      = 10000   # En pesos colombianos
DESCUENTO          = 0.15    # 15%

# --- Matriz del menú: [Nombre, Categoría, Precio Base] ---
menu = [
    ["Café Americano",   "Bebidas",   8000],
    ["Jugo de Naranja",  "Bebidas",   12000],
    ["Hamburguesa",      "Comidas",   25000],
    ["Ensalada César",   "Comidas",   18000],
    ["Limonada Natural", "Bebidas",   11000],
    ["Brownie",          "Postres",   9000],
]


# --- Módulo (función) requerido ---
def calcular_precio_final(producto):
    """
    Calcula el precio final de un producto aplicando
    el 15% de descuento si cumple AMBAS condiciones:
      - Pertenece a CATEGORIA_OBJETIVO
      - Su precio base supera UMBRAL_PRECIO
    Parámetros:
        producto: lista [Nombre, Categoría, Precio Base]
    Retorna:
        precio_final (float)
    """
    categoria = producto[1]
    precio    = producto[2]

    if categoria == CATEGORIA_OBJETIVO and precio > UMBRAL_PRECIO:
        precio_final = precio * (1 - DESCUENTO)
    else:
        precio_final = precio

    return precio_final


# --- Programa principal ---
print("=" * 57)
print("     MENÚ DEL RESTAURANTE - PROMOCIÓN APLICADA")
print("=" * 57)
print(f"{'Producto':<20} {'Categoría':<12} {'Precio Base':>11} {'Precio Final':>12}")
print("-" * 57)

for producto in menu:
    nombre       = producto[0]
    categoria    = producto[1]
    precio_base  = producto[2]
    precio_final = calcular_precio_final(producto)

    print(f"{nombre:<20} {categoria:<12} ${precio_base:>9,.0f} ${precio_final:>10,.0f}")

print("=" * 57)
print(f"\nPromoción activa: 15% de descuento en '{CATEGORIA_OBJETIVO}'")
print(f"Condición: precio base mayor a ${UMBRAL_PRECIO:,}")