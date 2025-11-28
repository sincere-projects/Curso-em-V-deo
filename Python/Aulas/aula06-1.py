# Isso pode ser útil para idenficar se tem texto talvez? Ou algo dentro

# n = bool(input("Digite algo: ")) //
n = input("Digite algo: ")
# print(n)
print(f"{bool(n)} - Bool") 
# True - Contém algo
# False - Vazio

# str(n)
# Testes de tipos
print(f"{n.isnumeric()} - Int") # Verificar se é Número 
print(f"{n.isalpha()} - String") # Verificar se é Letra
print(f"{n.isalnum()} - String and Int") # Verificiar se tem letra e número

# Tomei um erro gostoso agora
# Obs.: erro foi corrigido, mas estou notando que é melhor converter o valor se necessário
# invés de já converter no início do input
