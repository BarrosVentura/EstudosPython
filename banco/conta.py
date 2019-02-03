from cliente import Cliente

class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def sacar(self, quantidade):
        if self.saldo > 0 and (self.saldo - quantidade) >= 0 :
            self.saldo = self.saldo - quantidade
            print(quantidade, 'Retirados com sucesso!')
        else:
            print('Você não tem saldo o suficiente!')
    
    def depositar(self, quantidade):
        if self.saldo < self.limite and (self.saldo + quantidade) <= self.limite:
            self.saldo += quantidade
            print(quantidade, 'Adicionados com sucesso!')
        else:
            print('Você não pode mais adicionar fundos')

    def consulta(self):
        print('Seu saldo atual é de', self.saldo)
        