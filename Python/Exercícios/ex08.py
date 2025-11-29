""" # Desafio 08
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
e milímetros.
"""

print("Lembrete: não é nececssário colocar nada, apenas o número.")
print("="*30)

valor_metros = float(input("Digite apenas o valor em metros: "))
convert_cm = valor_metros * 100
convert_mm = valor_metros * 1000

print("")
print(f"Metros: {valor_metros}m")
print(f"Valor em centímetros: {convert_cm}cm")
print(f"Valor em milímetros: {convert_mm}mm")

print("="*30)

# Delícia tranquila de exercício
# Finalizado OK
