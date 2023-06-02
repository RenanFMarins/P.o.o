class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial):
        self.__numero_conta = numero_conta
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def consultar_saldo(self):
        return self.__saldo
    

conta = ContaBancaria("3214", 2000)

print(conta.consultar_saldo())

conta.depositar(50)
print(conta.consultar_saldo())

conta.sacar(20)
print(conta.consultar_saldo())

conta.sacar(200)