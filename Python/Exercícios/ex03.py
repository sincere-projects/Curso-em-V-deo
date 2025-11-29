'''
-> Desafio 3

Crie um programa que leia dois números e mostre a soma entre eles

'''

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")
soma = int(num1) + int(num2)

print(f"Resultado da soma: {num1} + {num2} = {soma}")
# Resultado OK

# Bom dia, começando a assistir resolução do Exercício 3
# 08:06am - 29/11/2025

print('--- Aula de Resolução ---')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2

print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
# Notei uma coisa boba, embora o primeiro jeito que estou aprendendo no Coddy.Tech
# A utilização do .format no final, fica parecendo mais organizada e sem exibir onde
# ficaria a váriavel, mas lógicamente seguindo em ordem colocada. 
# Então provável eu use mais o .format futuramente e sem ser vagabundo preguiçoso em usar
# o fzinho.