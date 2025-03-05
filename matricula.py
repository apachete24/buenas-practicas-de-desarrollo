import re
#cadena = "cadena de pruebas E1234 AAA, 1234BBBakdnjwnkwn"
cadena = input().strip()
regex = r"\bE?[\s-]?\d{4}[\s-]?[A-Z]{3}\b"
matchs = re.findall(regex, cadena)

for match in matchs:
    print(match)