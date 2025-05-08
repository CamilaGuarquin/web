# ESCRIBE ESTA LINEA DE CÓDIGO
print("Bievenidos al entrenamiento con python, vamos a disfrutar al máximo esta sesión")

"""
    Descuento en una compra:
    si compras más de $1000, obtienes un descuento del 20%
    pide el monto de la compra y muestra el precio final
"""

# Pedir datos por teclado al usuario int (Entero) float (Decimales) str (Cadenas de caracteres) bool (boleno unos o ceros)

compra = float(input("Por favor digita el valor de tu compra: "))
# si compras mas de $1000, obtienes un descuento del 20%
# Siempre que la salida tenga más de un camino de resolución, debo implementar condicionales
# operadores combinados
# operadores de asignación =, operadores aritméticos + - * /, operadores lógicos an y, or o, not
# operadores de comparación ==,!=,<,>=,<=

if compra > 1000: 
    descuento = compra * 0.2
    compra -= descuento
    #compra = compra - descuento
    print(f"el descuento es de {descuento}, por lo tanto su valor a pagar es: {compra}")
    
