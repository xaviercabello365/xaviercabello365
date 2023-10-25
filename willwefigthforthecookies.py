"""
Xavier Cabello
UF1 MO1
25/10/2023
"""

entrada = input("introduiex numero de persones y galetes junt amb un espai :")
num_personas, num_galletas = map(int, entrada.split())


if num_galletas % num_personas == 0:
    print("Let's Eat!")
else:
    print("Let's Fight")





