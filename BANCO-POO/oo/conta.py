class Historico:
    def __init__(self):
        self.historico = []  

    def gravar(self, operacao, valor):
        self.historico.append({"operacao": operacao, "valor": valor})


class Cliente:
    def __init__(self, nome: str, sobrenome: str, cpf: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Data:
    def __init__(self, dia: int, mes: int, ano: int):
        self.dia = dia
        self.mes = mes
        self.ano = ano


class Conta:
    def __init__(self, numero: str, titular: Cliente, saldo: float, limite: float, data_abertura: Data):
        self.numero = numero
        self.titular = titular  
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura  
        self.historico = Historico()  

    def depositar(self, valor):
        self.saldo += valor
        self.historico.gravar("Depósito", valor)

    def saca(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente para saque!")
            return False
        else:
            self.saldo -= valor
            self.historico.gravar("Retirada", valor)
            return True

    def extrato(self):
        print(f"Conta: {self.numero}")
        print(f"Saldo: R${self.saldo:.2f}")
        print(f"Titular: {self.titular.nome} {self.titular.sobrenome}")
        print(f"CPF: {self.titular.cpf}")
        print(f"Data de abertura: {self.data_abertura.dia}/{self.data_abertura.mes}/{self.data_abertura.ano}")
        print("Histórico de operações:")
        for operacao in self.historico.historico:
            print(f"- {operacao['operacao']}: R${operacao['valor']:.2f}")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            print("Transferência não realizada. Saldo insuficiente!")
            return False
        else:
            destino.depositar(valor)
            self.historico.gravar(f"Transferência para a conta {destino.numero}", valor)
            print(f"Transferência de R${valor:.2f} realizada para a conta {destino.numero}.")
            return True
