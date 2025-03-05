import re

cadena = input().strip()

regex = r"\b\d{4}\b"
matchs = re.findall(regex, cadena)

print("\n".join(matchs))


