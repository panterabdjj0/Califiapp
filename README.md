# CalifiApp

Aplicación de consola para registrar alumnos y consultar sus calificaciones.

Proyecto Scrum del **Submódulo 2: Aplica metodologías ágiles para el desarrollo de software**. CBTIS No. 200 · Programación · 3AM PGR.

## Objetivo del Sprint 1

Que el usuario pueda ver la lista completa de su grupo en orden alfabético y consultar los parciales, promedio y estatus de un alumno.

## Equipo Scrum

Integrantes registrados en el repositorio del equipo.

| Rol | Integrante |
|---|---|
| Product Owner | Emmanuel Cruz Luna |
| Scrum Master | Angel Juarez Torres |
| Equipo de desarrollo | Jesus Nahil |

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

Abre PowerShell dentro de la carpeta `califiapp` y escribe:

```powershell
python src/main.py
```

Si `python` no se reconoce, prueba `py src/main.py`.

## Cómo correr las pruebas

```powershell
python -m unittest discover -s tests -v
```

Resultado esperado: **Ran 18 tests** y **OK**.

## Estructura del proyecto

```text
califiapp/
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

## Git: commits sugeridos para registrar el trabajo

El cuaderno propone separar el trabajo en cinco commits. Después de revisar cada cambio y ejecutar las pruebas:

```powershell
git add .
git commit -m "HU-05: lista_ordenada y linea_lista (con 3 pruebas)"

git add .
git commit -m "HU-05: opción 5 del menú muestra la lista ordenada"

git add .
git commit -m "HU-06: buscar_alumno (con 2 pruebas) y refactor de nombre_repetido"

git add .
git commit -m "HU-06: opción 6 consulta a un alumno"

git add .
git commit -m "README: Sprint 1, HU-05 y HU-06, 18 pruebas"
```

Los commits son ejemplos de mensajes: Git no permite crear cinco commits retrospectivos idénticos si todos los cambios ya están juntos. Para conservar la trazabilidad, se deben hacer por separado mientras se desarrolla.

## Nota sobre los datos

En esta versión, `alumnos` y `calificaciones` se guardan en memoria. Se borran al cerrar el programa. El guardado permanente queda como trabajo del Sprint 2.
