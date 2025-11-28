# Sim, não tenho vergonha na cara e estou pulando a teoria e indo direto ao código, rs.
# Aula 06 - Tipos primitivos e Saída de Dados

'''  --- Lembretes ---

-> Sobre o Input e Valores

Obs.: Se definir um input sem definir o tipo será automáticamente 
considerado uma string. Portanto ele irá conectar ambas invés de somar ou realizar 
algo desejado. Por exemplo:

* Errado *
n1 = input('Digite um número: ')

* Correto *
n1 = int(input ('Digite um número: '))

-> Valores e Tipos

Int (Inteiro, números sem pontos)
Float (Flutuante, número reais)
Bool (True e False) # não use letra minúscula no começo
Str (texto) # sendo '' ou "" estando dentro de aspas simples ou duplas.

'''

n1 = input('Digite um número: ')
print(type(n1))

# Como não quero refazer o n1 com outro nome, vou testar tentando colocar 
# o n1 como int dentro do int() para tentar convertar
print(type(int(n1))) # Feedback: deu certo, retornou class: int

n2 = int(input('Digite um número: '))
n3 = int(input('Digite outro número: '))

print(f"A soma entre {n2} + {n3} = {n2 + n3}")
# Ou 
s = n2 + n3 # Talvez seja melhor ser feito assim? Caso eu deseje deixar dinamico?
print(f"A soma entre {n2} + {n3} = {s}")
# Não sei ainda, mas vou pensar sobre
