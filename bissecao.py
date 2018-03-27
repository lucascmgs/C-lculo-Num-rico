# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from Equation import Expression

tolerancia = (10 ** -6)

print("Insira a funcao a ser avaliada, tendo x como variavel.")

expressao = Expression(raw_input(), ["x"])

print("Insira o intervalo no qual a raiz esta situada")
inicio, fim = map(float, raw_input().split())

aprox = expressao((inicio + fim)/2)

crescente = False

if (expressao(inicio) < expressao(fim)):
    crescente = True

while(abs(fim - inicio) > tolerancia):
    meio = (inicio + fim)/2
    aprox = expressao(meio)
    if (aprox > 0 and crescente):
        fim = meio
    if (aprox > 0 and not crescente):
        inicio = meio
    if (aprox < 0 and crescente):
        inicio = meio
    if (aprox < 0 and not crescente):
        fim = meio
    
    print(inicio, fim) 

print("Final: ", meio, aprox)