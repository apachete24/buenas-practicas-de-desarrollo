import re

cadena = input().strip()

alumnos_regex = r"\b\w\.([a-z]+)\.(\d{4})@alumnos\.urjc\.es\b"
profesores_regex = r"\b([a-z]+)\.([a-z]+)@urjc\.es\b"


alumnos = re.findall(alumnos_regex, cadena)
profesores = re.findall(profesores_regex, cadena)



for apellido, year in alumnos:
    print(f"alumno {apellido} matriculado en {year}")

for nombre, apellido in profesores:
    print(f"profesor {nombre} apellido {apellido}")


