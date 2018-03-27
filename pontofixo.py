# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from Equation import Expression

tolerancia = (10 ** -6)

print("Insira a funcao g a ser iterada, tendo x como variavel.")

expressao = Expression(raw_input(), ["x"])

print("Insira o intervalo no qual a raiz esta situada")
inicio, fim = map(float, raw_input().split())


aprox = (fim - inicio)/2
aproxnova = expressao(aprox)

crescente = False


while(abs(aproxnova - aprox) > tolerancia):
    aprox = aproxnova
    aproxnova = expressao(aproxnova)
    
    print(aprox, aproxnova) 

print("Final:", aproxnova)