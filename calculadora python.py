#calculadora de python - terminal
#teste de interface cmd
import time
import sys
import os

print("Calculadora Python // by jaoocaminhao")
time.sleep(1.7)
print("\n")

inicio = print("Digite a opção desejada:\n 1- Soma\n 2- Subtração\n 3- Multiplicação\n 4- Divisão")
print("\n")

opcao = int(input("-> "))
print("\n")


#funções matematicas definidas
def soma(A,B):
    resultado01 = A + B
    print(f"O resultado da soma é: {resultado01}")

def sub(A,B):
    resultado02 = A - B
    print(f"O resultado da subtração é: {resultado02}")
    
def mult(A,B):
    resultado03 = A * B
    print(f"O resultado da multiplicação é: {resultado03}")
    
def div(A,B):
    resultado04NR = A / B
    resultado04 = round(resultado04NR, 2)
    print(f"O resultado da divisão é: {resultado04}")
    
#função de restart
    
#definicao da função de operação
if opcao == 1:
    
    print("_ + _")
    A = int(input("Digite o primeiro valor: "))
    print("\n")
    
    print(f"{A} + _")
    B = int(input("Digite o segundo valor: "))
    print("\n\n")

    print(f"{A} + {B}")
    soma(A,B)
    input("Aperte qualquer tecla para fechar! ")
    
elif opcao == 2:
    
    print("_ - _")
    A = int(input("Digite o primeiro valor: "))
    print("\n")
    
    print(f"{A} - _")
    B = int(input("Digite o segundo valor: "))
    print("\n\n")

    print(f"{A} - {B}")
    sub(A,B)
    input("Aperte qualquer tecla para fechar! ")
    
elif opcao == 3:
    
    
    print("_ x _")
    A = int(input("Digite o primeiro valor: "))
    print("\n")
    
    print(f"{A} x _")
    B = int(input("Digite o segundo valor: "))
    print("\n\n")

    print(f"{A} x {B}")
    mult(A,B)
    input("Aperte qualquer tecla para fechar! ")
    
elif opcao == 4:
    
    print("_ ÷ _")
    A = int(input("Digite o primeiro valor: "))
    print("\n")
    
    print(f"{A} ÷ _")
    B = int(input("Digite o segundo valor: "))
    print("\n\n")

    print(f"{A} ÷ {B}")
    div(A,B)
    input("Aperte qualquer tecla para fechar! ")
    
else:
    print("Tente novamente e digite um dos valores informados!!")
    time.sleep(1.2)
    
#contagem timer    
    i = 10
    while i in range(1,11):
        print(f"O programa se encerrará em {i} segundos", end="\r")
        i = i - 1
        time.sleep(1)
        
    if i == 0:
        sys.exit()