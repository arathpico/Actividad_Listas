# Programa para invertir el orden de los elementos en una lista
def invertir_lista():
    print("--- Invertir Elementos de una Lista ---")
    
    entrada = input("Ingresa elementos (números o palabras) separados por espacios: ")
    elementos = entrada.split()
    
    # Invertir la lista usando slicing [::-1]
    lista_invertida = elementos[::-1]
    
    print(f"\nLista original: {elementos}")
    print(f"Lista invertida: {lista_invertida}")

if __name__ == "__main__":
    invertir_lista()
