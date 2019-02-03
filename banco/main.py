from cliente import Cliente
from conta import Conta

primeiro_cliente = Cliente('Adson', 1223339485, 22)

primeira_conta = Conta(primeiro_cliente, 200, 1500)

print(primeiro_cliente.nome)
print(primeira_conta.cliente.nome)

primeira_conta.depositar(250)
primeira_conta.consulta()