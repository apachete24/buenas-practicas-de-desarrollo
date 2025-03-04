import re

cadena = input().strip()

regex = r"\d{4}+(?=\.?)"
matchs = re.findall(regex, cadena)

print("\n".join(matchs))


