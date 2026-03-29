from heapq import heappush, heappop
#heappush y heappop se utilizan para manejar una cola de prioridad, 
# lo que es esencial para la implementación del algoritmo de Dijkstra .
#en el sistema de transporte ayudará a gestionar eficientemente las rutas y los tiempos de viaje,
# asegurando que se seleccione la ruta más rápida entre dos estaciones.

#SISTEMA DE TRANSPORTE MASIVO LOCAL 
#Actividad 2: Implementación de un sistema de rutas a partir de una base de conocimiento escrito en reglas lógicas


#grafo

grafo = {
    "portal_cuba": [("megacentro", 8, "estación")],
    "megacentro": [("viajero", 4, "estación")],
    "viajero": [("terminal", 6, "estación"), ("dosquebradas", 7, "estación")],
    "terminal": [("utp", 10, "alimentador")],
    "dosquebradas": [("viajero", 7, "estación"), ("utp", 12, "alimentador")],
    "utp": [("dosquebradas", 12, "alimentador")]
}


def mejor_ruta(grafo, inicio, destino):
    
    # Implementación tipo Dijkstra con reglas lógicas para Minimizar tiempo
  
    cola = []
    heappush(cola, (0, inicio, [], None, 0))  
    
    visitados = {}

    while cola:
        costo, nodo, ruta, tipo_anterior, transbordos = heappop(cola)

        if nodo in visitados and visitados[nodo] <= costo:
            continue

        visitados[nodo] = costo
        ruta = ruta + [nodo]

        # Meta alcanzada
        if nodo == destino:
            return {
                "ruta": ruta,
                "tiempo_total": costo,
                "transbordos": transbordos
            }

        # Expandir nodos vecinos
        for vecino, tiempo, tipo_actual in grafo.get(nodo, []):
            
            nuevo_costo = costo + tiempo 

            nuevos_transbordos = transbordos
            if tipo_anterior and tipo_actual != tipo_anterior:
                nuevos_transbordos += 1

            heappush(cola, (
                nuevo_costo,
                vecino,
                ruta,
                tipo_actual,
                nuevos_transbordos
            ))

    return None




def mostrar_resultado(resultado):
    if not resultado:
        print("No se encontró una ruta.")
        return

    print("\n===== MEJOR RUTA =====")
    print(" -> ".join(resultado["ruta"]))
    print(f"Tiempo total: {resultado['tiempo_total']} minutos")
    print(f"Transbordos: {resultado['transbordos']}")


def main():
    print("Sistema de rutas - Megabús Pereira\n")

    inicio = input("Ingrese estación de origen: ").strip().lower()
    destino = input("Ingrese estación de destino: ").strip().lower()

    if inicio not in grafo or destino not in grafo:
        print("Error: estación no válida.")
        return

    resultado = mejor_ruta(grafo, inicio, destino)
    mostrar_resultado(resultado)



if __name__ == "__main__":
    main()