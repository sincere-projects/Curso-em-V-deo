'''
-> Desafio 4

Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possíveis sobre ele.

'''

valorA = input("Digite algo para analisar: ")

print(f"Tipo número: {valorA.isnumeric()}")
print(f"Tipo número real: {valorA.isdecimal()}")
print(f"Tipo texto: {valorA.isalpha()}")
print(f"Tipo número, texto ou ambos: {valorA.isalnum()}")
print(f"Contém tudo letras minúsculas: {valorA.islower()}")
print(f"Contém tudo letras maiúsculas: {valorA.isupper()}")
print(f"Contém apenas espaço: {valorA.isspace()}")

# Tomei outro erro, mas de dano mental, esqueci o ()
# fazendo retornar <built-in methoed> quase me desespero código mizeravi

# Resultado OK - Cansei por hoje e ta ótimo de dano psicológico
# 28/11/2025 - 16:31
