import re

cadena = input()

regex = r"(?<= )\d{4}-\d{2}-\d{2}(?= )"
matchs = re.findall(regex, cadena)

for i, fecha in enumerate(matchs):
    tmp = fecha.split('-')
    matchs[i] = f"{tmp[2]}.{tmp[1]}.{tmp[0]}"


print("\n".join(matchs))


