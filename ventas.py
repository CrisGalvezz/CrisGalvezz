import globales
import random

def cargar_ventas():
    ventas = globales.leer_archivo_json('ventas.json')
    empleados = globales.leer_archivo_json('empleados.json')
    id_ventas = 0
    try:
        for i in range(10):
            empleado = random.choice(empleados)
            venta = random.randint(150,500)*10000
            id_ventas += 1
            nombre_empleado = empleado['nombre']

            venta_random = {
                "nombre":nombre_empleado,
                "id_venta":id_ventas,
                "total_venta":venta,
            }

            ventas.append(venta_random)
        print("las ventas aleatorias han sido cargadas...")    
        globales.guardar_archivo_json('ventas.json', ventas)
    except:
        print("error al crear los archivos aleatorios...")
        
    
