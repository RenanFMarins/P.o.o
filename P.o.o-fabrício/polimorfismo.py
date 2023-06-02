class ContaBancaria:
    def __init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def exibir_saldo(self):
        print(f"Saldo disponível na conta {self.numero_conta}: R${self.saldo}")


class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Saldo disponível na conta corrente {self.numero_conta}: R${self.saldo}")


class ContaPoupanca(ContaBancaria):
    def calcular_juros(self, taxa):
        juros = self.saldo * (taxa / 100)
        self.saldo += juros
        print(f"Juros de R${juros} calculados e adicionados.")


contas = [ContaBancaria("123", 1000), ContaCorrente("456", 2000), ContaPoupanca("789", 5000)]


for conta in contas:
    conta.sacar(50)
    conta.exibir_saldo()
    print("-----------------------")
