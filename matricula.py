import re

cadena = input().strip()
regex = r"E?\d{4}[\s|-]?[A-Z]{3}"
matchs = re.findall(regex, cadena)

print(*matchs, sep="\n")