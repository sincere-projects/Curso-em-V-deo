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

# Resolução da aula - Exercício 04

print("--- Resolução da aula ---")
a = input("Digite algo: ")
print("O tipo primitivo desse valor é: {}".format(type(a))) # Esse eu não fiz kkk
print("Só tem espaço? {}".format(a.isspace())) # OK
print("É um número? {}".format(a.isalpha())) # OK
print("É alfanúmero? {}".format(a.isalnum())) # OK
print("Está em maiúsculas? {}".format(a.isupper())) # OK
print("Está em minúsculas? {}".format(a.islower())) # OK
print("Está capitalizada? {}".format(a.istitle())) # Não sabia o que era então não tinha feito

# Anotação: não sei o que é o istitle ou capitalizada, porém...
# parece estar verificando se a primeira letra está em maiúscula e o resto minúsculo
# semelhante a um título.
