# Programa para encontrar el número mayor y menor en una lista
def encontrar_mayor_menor():
    print("--- Encontrar Número Mayor y Menor ---")
    
    entrada = input("Ingresa números separados por espacios: ")
    numeros = [float(x) for x in entrada.split()]
    
    if not numeros:
        print("No ingresaste ningún número.")
        return

    # Inicializar con el primer elemento de la lista
    mayor = numeros[0]
    menor = numeros[0]
    
    # Recorrer la lista comparando cada número
    for num in numeros:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
            
    print(f"\nLista evaluada: {numeros}")
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")

if __name__ == "__main__":
    encontrar_mayor_menor()
