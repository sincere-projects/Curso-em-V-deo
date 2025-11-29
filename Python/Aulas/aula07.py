# Aula 07 - Operadores aritméticos
"""
Adição              +   | Potência          **
Subtração           -   | Divisão Inteira   //
Multiplicação       *   | Resto da Divisão  %
Divisão             /   | 

--- Anotações ---
Re-lembrando: potência, ela o valor. Portanto seria X elevado por Y. Por exemplo:
10 x 10 (sendo ele multiplicando por ele mesmo)

- 10 elevado a 5 
10 x 10 x 10 x 10 x 10

Divisão inteira retorna o valor inteiro que retorna na conta (sem virgulas ou número reais)
Resto da divisão retorna o valor restante "o resto que sobrou".

- Ordem de Precedenência -
1 - ()
2 - **
3 - *  /  //  %
4 - +  -

- Aprendizagem -
O pow(x, y) faz o mesmo trabalho que usar o **

Agora diferente e sem ser números, mas utilizando strings.
Utilizando o 'texto' + 'acabou' irá retornar 'textoacabou'
Outros exemplos: 'Oi' * 5 retornar 5 Oi todos juntos
'=' * 20 retornando um linha de =

"""

# Pausa pro café - 08:35
# Voltei 09:05

nome = input("Qual é o seu nome?")
print("Prazer em te conhecer {:=^20}".format(nome))

# :20 irá criar um espaço de 20 caracteres / o que seria letras ou espaços.
# :>20 fará o alinhamento a direita
# :<20 alinhado a esquerda
# :^20 centralizado em 20 espaços
# :=^20 fará o nome centralizado e com o "=" em volta

n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# print("A soma vale {}".format(n1+n2))
# Usar outra variável para caso for utilizar em outro lugar
print("A soma é {}, o produto é {} e a divisão é {:.3f}".format(s, m, d), end = ' ')
# Para formatar os valores, utilize :.xf
# o f representa o valor flutuante
# end = "" ele faz que o outro print apareça na mesma linha que o próximo print deveria
# ser em outra.
# \n - realiza a quebra de linha
print("Divisão Inteira {} e potência {}".format(di, e))

