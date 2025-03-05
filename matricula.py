import re

cadena = input().strip()
regex = r"\bE?[\s-]?\d{4}[\s-]?[A-Z]{3}\b"
matchs = re.findall(regex, cadena)

print(*matchs, "\n")