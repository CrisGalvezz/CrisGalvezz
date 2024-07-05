import globales
import ventas
import estadisticas
def menu():
    while True:
        print("1. Asignar ventas aleatorias.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa")
        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            ventas.cargar_ventas()
        if opcion == 2:
            while True:
                print("1. Venta más alta.")
                print("2. Venta más baja.")
                print("3. Promedio de ventas.")
                print("4. Medio Geometrica.")
                print("5. Atras")
                opcion = globales.seleccionar_opcion(5)
                if opcion == 1:
                    estadisticas.venta_mas_alta()
                if opcion == 2:
                    estadisticas.venta_mas_baja()
                if opcion == 3:
                    estadisticas.promedio_ventas()
                if opcion == 4:
                    estadisticas.media_geometrica()
                if opcion == 5:
                    print("volviendo...")
                    break

        if opcion == 3:
            print("Salir")
            break
            

menu()