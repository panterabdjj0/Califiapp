# CalifiApp - Proyecto Scrum del CBTIS 200
# Ejecutar desde la carpeta califiapp con: python src/main.py

from calificaciones import (LIMITE_ALUMNOS, registrar_alumno, nombre_repetido,
                            validar_calificacion, calcular_promedio, obtener_estatus,
                            fila_reporte, promedio_grupal,
                            lista_ordenada, linea_lista, buscar_alumno)

NOMBRE_APP = "CalifiApp"
OBJETIVO = "Registrar y consultar las calificaciones de un grupo"
PARCIALES = 3

alumnos = []
calificaciones = {}


# HU-01 Registrar alumnos
def opcion_registrar():
    print("\nREGISTRAR ALUMNOS (deja el nombre vacío para terminar)")
    while True:
        nombre = input("Nombre del alumno: ")
        if nombre.strip() == "":
            break
        if nombre_repetido(alumnos, nombre):
            print("  Ese alumno ya está registrado. Escribe otro nombre.")
        elif registrar_alumno(alumnos, nombre):
            print("  Registrado. Total:", len(alumnos), "de", LIMITE_ALUMNOS)
        else:
            print("  No se pudo registrar: el grupo ya tiene", LIMITE_ALUMNOS, "alumnos.")
            break


# HU-02 Capturar calificaciones
def opcion_capturar():
    if len(alumnos) == 0:
        print("\nPrimero registra alumnos (opción 1).")
        return
    print("\nCAPTURAR CALIFICACIONES (de 0 a 10)")
    for nombre in alumnos:
        parciales = []
        print("Alumno:", nombre)
        while len(parciales) < PARCIALES:
            texto = input("  Parcial " + str(len(parciales) + 1) + ": ")
            calificacion = validar_calificacion(texto)
            if calificacion is None:
                print("  Calificación no válida. Escribe un número de 0 a 10.")
            else:
                parciales.append(calificacion)
        calificaciones[nombre] = parciales


# Refactor de PG7: HU-03 y HU-04 usan el mismo cálculo
def promedios_del_grupo():
    resultado = []
    for nombre in alumnos:
        if nombre in calificaciones:
            promedio = calcular_promedio(calificaciones[nombre])
            resultado.append((nombre, promedio))
    return resultado


# HU-03 Calcular promedio y estatus
def opcion_promedios():
    if len(calificaciones) == 0:
        print("\nPrimero captura calificaciones (opción 2).")
        return
    print("\nPROMEDIO Y ESTATUS")
    for nombre, promedio in promedios_del_grupo():
        print(" ", nombre, "->", promedio, obtener_estatus(promedio))


# HU-04 Mostrar reporte del grupo
def opcion_reporte():
    if len(calificaciones) == 0:
        print("\nPrimero captura calificaciones (opción 2).")
        return
    print("\nREPORTE DEL GRUPO")
    print("-" * 50)
    print("Alumno | Promedio | Estatus")
    print("-" * 50)
    promedios = []
    for nombre, promedio in promedios_del_grupo():
        promedios.append(promedio)
        print(fila_reporte(nombre, promedio))
    print("-" * 50)
    print("Promedio grupal:", promedio_grupal(promedios))
    print("Total de alumnos en el reporte:", len(promedios))


# HU-05 Mostrar lista alfabética
def opcion_lista():
    if len(alumnos) == 0:
        print("\nAún no hay alumnos registrados (opción 1).")
        return
    print("\nLISTA DEL GRUPO (orden alfabético)")
    print("-" * 50)
    numero = 1
    for nombre in lista_ordenada(alumnos):
        print(linea_lista(numero, nombre))
        numero = numero + 1
    print("-" * 50)
    print("Total:", len(alumnos), "de", LIMITE_ALUMNOS, "alumnos")


# HU-06 Consultar a un alumno
def opcion_consultar():
    if len(alumnos) == 0:
        print("\nAún no hay alumnos registrados (opción 1).")
        return
    texto = input("\nNombre del alumno a consultar: ")
    nombre = buscar_alumno(alumnos, texto)
    if nombre is None:
        print(" No encontré a", texto.strip(), "en el grupo. Revisa la lista (opción 5).")
        return
    print("\nCONSULTA DE", nombre)
    if nombre not in calificaciones:
        print(" Aún no tiene calificaciones (opción 2).")
        return
    parciales = calificaciones[nombre]
    numero = 1
    for calificacion in parciales:
        print(" Parcial " + str(numero) + ": " + str(calificacion))
        numero = numero + 1
    promedio = calcular_promedio(parciales)
    print(" Promedio:", promedio, obtener_estatus(promedio))


# Menú principal
def main():
    opcion = ""
    while opcion != "0":
        print("\n" + "=" * 50)
        print("  " + NOMBRE_APP + " - " + OBJETIVO)
        print("=" * 50)
        print("  1. Registrar alumnos             (HU-01)")
        print("  2. Capturar calificaciones       (HU-02)")
        print("  3. Calcular promedio y estatus   (HU-03)")
        print("  4. Mostrar reporte del grupo     (HU-04)")
        print("  5. Ver lista del grupo            (HU-05)")
        print("  6. Consultar a un alumno          (HU-06)")
        print("  0. Salir")
        print("-" * 50)
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            opcion_registrar()
        elif opcion == "2":
            opcion_capturar()
        elif opcion == "3":
            opcion_promedios()
        elif opcion == "4":
            opcion_reporte()
        elif opcion == "5":
            opcion_lista()
        elif opcion == "6":
            opcion_consultar()
        elif opcion == "0":
            print("Gracias por usar " + NOMBRE_APP + ". ¡Hasta pronto!")
        else:
            print("\nOpción no válida. Escribe un número del 0 al 6.")

        if opcion != "0":
            input("\nPresiona ENTER para volver al menú...")


if __name__ == "__main__":
    main()
