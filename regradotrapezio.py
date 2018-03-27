# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from Equation import Expression

tolerancia = (10 ** -6)

print "Insira a funcao g que de que se quer calcular a integral, tendo x como variavel."

expressao = Expression(raw_input(), ["x"])

print "Insira o início e o fim do intervalo, além do passo"
inicio, fim, passo = map(float, raw_input().split())



resultado = expressao(inicio)
atual = inicio + passo
while atual != fim :
    print atual, expressao(atual)
    resultado += 2 * expressao(atual)
    atual += passo
print atual, expressao(atual)
resultado += expressao(fim)

print resultado

resultado = resultado * passo / 2

print resultado