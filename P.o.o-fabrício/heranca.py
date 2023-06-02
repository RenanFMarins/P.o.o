class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial):
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Saldo disponível na conta {self.numero_conta}: R${self.saldo}")


class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, saldo_inicial, limite):
        super().__init__(numero_conta, saldo_inicial)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def exibir_saldo(self):
        print(f"Saldo disponível na conta corrente {self.numero_conta}: R${self.saldo}")
        print(f"Limite da conta corrente: R${self.limite}")


class ContaPoupanca(ContaBancaria):
    def calcular_juros(self, taxa):
        juros = self.saldo * (taxa / 100)
        self.saldo += juros
        print(f"Juros de R${juros} calculados e adicionados à conta.")


# conta bancária
conta = ContaBancaria("3214", 2000)
conta.depositar(1000)
conta.sacar(200)
conta.exibir_saldo()

# conta corrente
conta_corrente = ContaCorrente("5678", 2000, 1000)
conta_corrente.depositar(1000)
conta_corrente.sacar(3000)
conta_corrente.exibir_saldo()  

# conta poupança
conta_poupanca = ContaPoupanca("9012", 5000)
conta_poupanca.depositar(1000)
conta_poupanca.calcular_juros(2)
conta_poupanca.exibir_saldo()
