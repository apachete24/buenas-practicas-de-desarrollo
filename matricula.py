import re
'''
cadena = "KDJ1234AAA E1234-BBBE1234CCCWEIFIksdj-24214a wdqw"
regex = r"E?\d{4}[\s|-]?[A-Z]{3}"
matchs = re.findall(regex, cadena)

print(matchs)

'''

cadena = input()
regex = r"E?\d{4}[\s|-]?[A-Z]{3}"
matchs = re.findall(regex, cadena)

print(matchs)