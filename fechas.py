import re

cadena = input().strip()
regex = r"\b(\d{4})-(\d{2})-(\d{2})\b"

matchs = re.sub(regex, r"\3.\2.\1", cadena)


print(matchs)