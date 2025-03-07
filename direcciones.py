import re

#cadena = "Calle Nombre, Nº 10, 76540"
cadena = input().strip()

regex=r"\b(C/|Calle)\s([A-ZÑ][a-zñ]+),?\s+(Nº|nº|N|n)?\s?(\d+),\s+(\d{5})\b"
matchs = re.findall(regex, cadena)


#print(matchs)

for _, nombre, _, numero, cp in matchs:
    print(f"{cp}-{nombre}-{numero}")
