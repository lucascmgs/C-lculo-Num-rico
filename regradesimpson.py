# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from Equation import Expression

tolerancia = (10 ** -6)

print "Insira a funcao g que de que se quer calcular a integral, tendo x como variavel."

expressao = Expression(raw_input(), ["x"])

print ("Insira o início e o fim do intervalo, além do passo")
inicio, fim, passo = map(float, raw_input().split())



resultado = expressao(inicio)
print inicio, expressao(inicio)
atual = inicio + passo
controle = 0
while atual != fim :
    print atual, expressao(atual)
    if controle % 2 == 0:
        resultado += 4*expressao(atual)
    if controle % 2 == 1:
        resultado += 2*expressao(atual)
    controle += 1
    atual += passo   
print atual, expressao(atual)
resultado += expressao(fim)

print resultado

resultado = resultado * passo / 3

print resultado