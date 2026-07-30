# Programa para calcular la suma de los elementos de una lista
def sumar_elementos():
    print("--- Suma de Elementos de una Lista ---")
    
    # Pedir los elementos de la lista
    entrada = input("Ingresa números separados por espacios: ")
    numeros = [float(x) for x in entrada.split()]
    
    # Calcular la suma recorriendo la lista
    suma_total = 0
    for num in numeros:
        suma_total += num
        
    print(f"\nLista de números: {numeros}")
    print(f"La suma total de los elementos es: {suma_total}")

if __name__ == "__main__":
    sumar_elementos()
