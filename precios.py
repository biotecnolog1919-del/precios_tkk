def up_ganancia(precio_base):
    total = (precio_base * 100) / 69
    return total


def down_ganancia(precio_base):
    suma = precio_base * 1.113
    total = (suma * 100) / 69
    return total


def primera_fase_comparar(precio_base):
    if precio_base >= 500:
        return up_ganancia(precio_base)
    else:
        return down_ganancia(precio_base)   

   
while True:  
  precio_base = int(input("Ingresa el precio base: "))
  resultado = primera_fase_comparar(precio_base)
  print(f"Precio TTI: ${resultado:.2f}") 

  