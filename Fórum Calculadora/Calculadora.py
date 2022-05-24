from xmlrpc.client import boolean
import operator
import math


class Calculadora:

    # O primeiro passo é adicionar um valor mutável que irá armazenar o resultado das operações.
    # Este valor, que chamarei de i, deve iniciar com 0 e ter a capacidade de ser resetado. 

    i = 0
    def resetIndex(self):
        self.i = 0

    # O módulo operator foi importado para definir um "dicionário" de operações aritiméticas

    operador = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow,
        '//': operator.floordiv
    }

    # Para fazer as operações, foi criado um módulo chamado "calculo", que irá requisitar os valores
    # e as operações a serem realizadas ao usuário, além de realizar os cálculos necessários.

    def calculo(self):
        print("Para finalizar o programa, aperte 'enter' sem digitar uma operação")
        
        # Requisita o valor de X.
        x = input("Digite um valor: ")
        
        # Caso o valor retorne nulo, irá requisitar o valor novamente.
        if x == "":
            while x == "":
                x = input("Digite um valor: ")
        x = float(x)

        # Esta variável irá guardar o valor de 'operacao'.
        op = 0

        # Aqui inicializo y para evitar erros.
        y = 0

        # Aqui começa os cálculos.
        # Está dentro de um while pois você pode realizar operações com o resultado da anterior.
        while x != "":
            operacao = input("Digite a operação (+, -, *, /, %, **, //, =, sqr): ")
            
            # Caso o usuário inserir '=' como operação, o programa irá executar a operação anterior com o resultado mais recente.
            if operacao == "=" and op == 0:
                print("Operação inválida")
                continue

            if operacao == "=" and op != 0:
                self.i = self.operador[op](x,y)
                print(calculadora.i)
                x = self.i
                continue

            # Realiza a raíz quadrada utilizando o módulo math que foi importado.
            if operacao == "sqr":
                self.i = math.sqrt(x)
                print(calculadora.i)
                x = self.i
                continue

            # Caso não insira nenhum valor em operacao, o programa será finalizado.
            if operacao == "":
                print("Operação finalizada")
                break

            # Requisita o valor de Y.
            y = input("Digite um valor: ")
            if y == "":
                y = 0
            y= float(y)
            op = operacao
            
            # Realiza as operações aritiméticas utilizando o módulo operator que foi importado.
            if operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/" or operacao == "%" or operacao == "**" or operacao == "//":
                self.i = self.operador[operacao](x,y)
            
            # Caso operacao não possua um valor válido, a aplicação pedirá para digitar novamente.
            else:
                print("Operação inválida")
                continue

            # Mostra o resultado da operação no output
            print(calculadora.i)
            x = self.i
        
# Agora é só executar a classe e chamar o módulo.

calculadora = Calculadora()

calculadora.calculo()

# Eu empolguei. (Queria fazer mais só que fiquei com fome e acabei parando)







