# Programa para contar números pares e impares en una lista
def contar_pares_impares():
    print("--- Contador de Pares e Impares ---")
    
    # Pedir al usuario los números separados por espacio
    entrada = input("Ingresa una lista de números enteros separados por espacios: ")
    
    # Convertir la entrada en una lista de enteros
    numeros = [int(x) for x in entrada.split()]
    
    pares = 0
    impares = 0
    
    # Recorrer la lista para clasificar
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    print(f"\nLista ingresada: {numeros}")
    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")

if __name__ == "__main__":
    contar_pares_impares()
