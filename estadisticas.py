import globales, math

def venta_mas_alta():
    all_ventas = globales.leer_archivo_json('ventas.json')
    all_empleados = globales.leer_archivo_json('empleados.json')

    ventas_ordenadas = sorted(all_ventas, key=lambda x:x ['total_venta'], reverse=True)

    ventas_ordenadas = ventas_ordenadas[0]
    nombre_empleado = ventas_ordenadas['nombre']
    total_venta_maxima = ventas_ordenadas['total_venta']

    nombre_venta_mas_alta = ""
    try:
        for nombre in all_empleados:
            if nombre['nombre'] == nombre_empleado:
                nombre_venta_mas_alta = nombre['nombre']
                break
    except:
        print("error en la verificacion de la venta mas alta")

    print(f"{nombre_venta_mas_alta}, ${total_venta_maxima}")
    
def venta_mas_baja():
    all_ventas = globales.leer_archivo_json('ventas.json')
    all_empleados = globales.leer_archivo_json('empleados.json')
    ventas_ordenadas = sorted(all_ventas, key=lambda x:x ['total_venta'], reverse=False)

    ventas_ordenadas = ventas_ordenadas[0]
    nombre_empleado = ventas_ordenadas['nombre']
    venta_baja = ventas_ordenadas['total_venta']

    nombre_venta_mas_baja = ""
    try:

        for empleado in all_empleados:
            if empleado['nombre'] == nombre_empleado:
                nombre_venta_mas_baja = empleado['nombre']
                break
    except:
        print("error en la verificacion de la venta mas baja")

    print(f"{nombre_venta_mas_baja}, ${venta_baja}")

def promedio_ventas():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    cantidad = 0
    suma = 0
    try:
        for venta in todas_las_ventas:
            suma += venta['total_venta']
            cantidad += 1

        promedio = suma/cantidad
    except:
        print("error de verificacion del promedio de ventas")

    print(f"el promedio de las ventas es ${int(promedio)}")
def media_geometrica():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    cantidad = 0
    suma = 0
    try:
        for venta in todas_las_ventas:
            suma += math.log(venta['total_venta'])
            cantidad += 1

        media = math.exp(suma/cantidad)
    except:
        print("error en la media geometrica")

    print(f"La media geometrica de las ventas es ${int(media)}")

