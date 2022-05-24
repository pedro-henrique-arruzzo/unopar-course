from xmlrpc.client import boolean
import operator


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
        x = input("Digite um valor: ")
        if x == "":
            while x == "":
                x = input("Digite um valor: ")
        x = float(x)

        op = 0

        while x != "":
            operacao = input("Digite a operação (+, -, *, /, %, **, //): ")

            if operacao == "=":
                self.i = self.operador[op](x,y)
                print(calculadora.i)
                x = self.i
                continue

            if operacao == "":
                print("Operação finalizada")
                break

            op = operacao
            y = input("Digite um valor: ")
            y= float(y)
            
            if operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/" or operacao == "%" or operacao == "**" or operacao == "//":
                self.i = self.operador[operacao](x,y)
            
            else:
                print("Operação inválida")
                break

            print(calculadora.i)
            x = self.i
        
# Agora é só executar a classe e chamar o módulo.

calculadora = Calculadora()

calculadora.calculo()

# Eu empolguei. (Queria fazer mais só que fiquei com fome)







