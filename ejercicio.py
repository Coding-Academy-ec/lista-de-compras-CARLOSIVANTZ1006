# ejercicio.py

def convertir_lista_a_tupla(lista_compras):
    
    tupla_compras = tuple(lista_compras)
    return tupla_compras

# Ejemplo de uso
if __name__ == "__main__":
    compras_usuario = input("Ingresa los elementos de la lista de compras separados por comas: ")
    lista_compras = compras_usuario.split(", ")
    tupla_compras = convertir_lista_a_tupla(lista_compras)
    print("Lista de Compras:", tupla_compras)
