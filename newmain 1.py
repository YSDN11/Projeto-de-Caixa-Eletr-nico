# Criação da Classe Conta
# Aluno: Guilherme Costa: 03256644
# Faça o "import os from time import sleep"
# codigo feito em conjunto com o aluno Yan Silva: 03318157

import os
from time import sleep

class Conta:
    def __init__(self, cliente, cpf, agencia, numero, saldo):
        self.cliente = cliente
        self.cpf = cpf
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

# Definindo as funções, métodos utilizados no caixa:
    def extrato(self):
        print("Saldo da conta: R$ %.2f" % self.saldo)

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente para essa operação.")
            return False

    def deposita(self, valor):
        self.saldo += valor

    def transfere(self, cc_destino, valor):
        if self.saca(valor) == True:
            cc_destino.deposita(valor)

    def pix(self, cc_destino, valor):
        if self.saca(valor) == True:
            cc_destino.deposita(valor)

# Criando Contas para realizar e experimentar as funções do caixa:
minhaConta = Conta("Guilherme", "111333444-13", 123, 14, 0)
print(vars(minhaConta))
outraConta = Conta("Yan", "55566677-12", 456, 15, 0)
print(vars(outraConta))


# Aqui começa o Menu do caixa eletrônico:
while True:
    print("-" * 30)
    s = int(input('1 = Conta Guilherme\n2 = Conta Yan\n3 = Sair\nDeseja entrar em qual conta? ')) #Seleciona conta
    print("-" * 30)
    if s == 1:
        print("Bem-vindo Guilherme Costa Gomes") # Entrou na conta Guilherme
        while True:
            print("-"*30)
            print("Menu de opções:") # menu para escolher os métodos do caixa
            print("-"*30)
            print('1 = Extrato\n2 = Sacar\n3 = Depósito\n4 = Tranferência\n5 = Pix\n6 = Sair')
            print("-"*30)

            # Selecionar o método do caixa
            i = int(input("Selecione uma opção: "))
            if i == 1: # método de ver extrato
                os.system("cls")
                minhaConta.extrato()
                sleep(1)

            elif i == 2: # método de saque
                v = int(input("Qual o valor do saque? R$"))
                os.system("cls")
                minhaConta.saca(v)
                print("Saque efetuado com sucesso!")
                sleep(1)

            elif i == 3: # método de depósito
                v = int(input("Qual no valor do deposito? R$"))
                os.system("cls")
                minhaConta.deposita(v)
                print("Deposito efetuado com sucesso!")
                sleep(1)

            elif i == 4: # método de transferencia bancária
                v = int(input("Qual no valor da transferencia? R$"))

                if v > minhaConta.saldo:
                    print("Saldo insuficiente para essa operação.")

                else:
                    print("Para quem você deseja transferir?")
                    print("1 - Yan Silva do Nascimento\n2 - Sair")
                    q = int(input("Selecione uma opção: "))

                    if q == 1:
                        minhaConta.transfere(outraConta, v)
                        os.system("cls")
                        print("Transferência efetuada com sucesso!")
                        sleep(1)

                    elif q == 2:
                        print("Saindo!")
                        sleep(1)

                    else:
                        os.system("cls")
                        print("Opção inválida!")
                        sleep(1)

            elif i == 5: # método de pix (Chave CPF encontra-se no inicio do programa ao ser executado)
                v = int(input("Qual no valor da transferência? R$"))

                if v > minhaConta.saldo:
                    print("Saldo insuficiente para essa operação.")

                else:
                    p = int(input("Digite a chave pix usando somente números (CPF):"))
                    if p == 5556667712:
                        print("Transferindo para Yan Silva do Nascimento... Aguarde!")
                        sleep(2)
                        minhaConta.pix(outraConta, v)
                        print("Transferência efetuada com sucesso!")

                    else:
                        print("Chave não reconhecida!")

            else:
                break

    elif s == 2:
        print("Bem-vindo Yan Silva do Nascimento") # entrou na conta Yan Silva do Nascimento
        while True:
            print("-" * 30)
            print("Menu de opções:") # menu com as funções do caixa
            print("-" * 30)
            print('1 = Extrato\n2 = Sacar\n3 = Depósito\n4 = Tranferencia\n5 = Pix\n6 = Sair')
            print("-" * 30)

            i = int(input("Selecione uma opção: "))

            if i == 1: # método de ver extrato
                os.system("cls")
                outraConta.extrato()
                sleep(1)

            elif i == 2: # método de saque
                v = int(input("Qual o valor do saque? R$"))
                outraConta.saca(v)
                os.system("cls")
                print("Saque efetuado com sucesso!")
                sleep(1)

            elif i == 3: # método de depósito
                v = int(input("Qual no valor do deposito? R$"))
                outraConta.deposita(v)
                os.system("cls")
                print("Depósito efetuado com sucesso!")
                sleep(1)

            elif i == 4: # método de transferência
                v = int(input("Qual no valor da transferencia? R$"))

                if v > minhaConta.saldo:
                    print("Saldo insuficiente para essa operação.")

                else:
                    print("Para quem você deseja transferir?")
                    print("1 - Guilherme Costa Gomes\n2 - Sair")
                    q = int(input("Selecione uma opção: "))

                    if q == 1:
                        outraConta.transfere(minhaConta, v)
                        os.system("cls")
                        print("Transferência efetuada com sucesso!!")
                        sleep(1)

                    elif q == 2:
                        print("Saindo!")
                        sleep(1)

                    else:
                        print("Opção inválida")

            elif i == 5: # método de pix (Chave CPF encontra-se no inicio do programa ao ser executado
                v = int(input("Qual no valor da transferência? R$"))

                if v > minhaConta.saldo:
                    print("Saldo insuficiente para essa operação.")

                else:
                    p = int(input("Digite a chave pix usando somente números (CPF):"))
                    if p == 11133344413:
                        print("Transferindo para Guilherme Costa Gomes... Aguarde!")
                        sleep(2)
                        outraConta.pix(minhaConta, v)
                        print("Transferência efetuada com sucesso!")

                    else:
                        print("Chave não reconhecida!")

            else:
                break

    else:
        break