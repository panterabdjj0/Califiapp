# CalifiApp

Aplicación de consola para registrar alumnos y consultar sus calificaciones.

Proyecto Scrum del **Submódulo 2: Aplica metodologías ágiles para el desarrollo de software**. CBTIS No. 200 · Programación · 3AM PGR · Docente: Mtro. Omar Torres Sánchez.

## Objetivo del Sprint 1

Que el usuario pueda ver la lista completa de su grupo en orden alfabético y consultar los parciales, promedio y estatus de un alumno.

## Equipo Scrum

| Rol | Integrante |
|---|---|
| Product Owner | Emmanuel Cruz Luna |
| Scrum Master | Angel Juarez Torres |
| Equipo de desarrollo | Jesus Nahil |

Tablero del proyecto: pendiente de agregar el enlace de GitHub Projects del equipo.

## Historias de usuario

| HU | Historia | Estado |
|---|---|---|
| HU-01 | Registrar alumnos (máximo 30, sin nombres repetidos) | Terminada |
| HU-02 | Capturar calificaciones de 0 a 10 | Terminada |
| HU-03 | Calcular promedio y estatus (aprueba con 6) | Terminada |
| HU-04 | Mostrar reporte del grupo | Terminada |
| HU-05 | Ver la lista del grupo en orden alfabético con su total | Terminada (Sprint 1) |
| HU-06 | Consultar a un alumno: sus parciales y su promedio | Terminada (Sprint 1) |

## Sprint 1 (9 y 10 de noviembre de 2026)

**Incremento:** opciones 5 (HU-05) y 6 (HU-06) del menú, con 5 pruebas nuevas (18 en total).

**Lo que aprendimos en la Sprint Review:** los datos de alumnos y calificaciones viven en la memoria mientras el programa está abierto; al cerrar CalifiApp se pierden. Para el Sprint 2 se propone guardar la información en un archivo JSON o CSV (HU-07 por definir).

### Sprint Backlog: 8 tareas

| Tarea | Trabajo | Historia |
|---|---|---|
| T1 | Crear pruebas de lista ordenada | HU-05 |
| T2 | Programar lista_ordenada() y linea_lista() | HU-05 |
| T3 | Agregar opción 5 al menú | HU-05 |
| T4 | Crear pruebas de búsqueda | HU-06 |
| T5 | Programar buscar_alumno() y refactorizar nombre_repetido() | HU-06 |
| T6 | Agregar opción 6 al menú | HU-06 |
| T7 | Actualizar README y comprobar las 18 pruebas | Sprint 1 |
| T8 | Demostrar el incremento y registrar el descubrimiento | Sprint Review |

## Cómo ejecutar

Abre PowerShell dentro de la carpeta del proyecto y escribe:

```powershell
python src/main.py
```

Si `python` no se reconoce, prueba `py src/main.py`.

## Cómo correr las pruebas

```powershell
python -m unittest discover -s tests -v
```

Resultado comprobado: **Ran 18 tests** y **OK**.

## Estructura del proyecto

```text
Califiapp/
├── README.md
├── .gitignore
├── data/
├── src/
│   ├── main.py
│   └── calificaciones.py
└── tests/
    └── test_calificaciones.py
```

## Definición de Terminado (DoD)

- [x] Las funciones HU-05 y HU-06 cumplen los criterios programados.
- [x] Las pruebas automatizadas pasan: 18 tests y OK.
- [ ] Un compañero revisó el cambio antes del commit (requiere revisión real del equipo).
- [x] El README quedó actualizado.

## Commits del Sprint 1

- HU-05 y HU-06: agrega lista alfabética y búsqueda de alumnos.
- HU-05 y HU-06: agrega cinco pruebas automatizadas.
- HU-05 y HU-06: agrega opciones 5 y 6 al menú.
- README: documenta Sprint 1, HU-05, HU-06 y las 18 pruebas.

## Nota sobre los datos

En esta versión, `alumnos` y `calificaciones` se guardan en memoria. Se borran al cerrar el programa. El guardado permanente queda como trabajo del Sprint 2.
