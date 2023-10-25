"""
Xavier Cabello
UF1 MO1
25/10/2023
"""
#demanem un numero per sapiguer els dies de qualsevol mes de l'any
mes = int(input("Ingresa el número del mes (1-12): "))

dias_por_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

if mes >= 1 and mes <= 12:
    numero_de_dias = dias_por_mes[mes]
    print(f"El mes {mes} tiene {numero_de_dias} días.")
else:
    print("Número de mes inválido. Debe estar entre 1 y 12.")

