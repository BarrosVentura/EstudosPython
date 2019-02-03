'''
# 1ª
print('Ola Mundo')

#2ª
numero = input('digite o numero: ')
print('O número informado foi: ', numero)

#3ª
primeiro = int(input('Digite o primeiro numero'))
segundo = int(input('Digite o segundo número'))
soma = primeiro + segundo
print('A soma é:', soma)

#4º
primeira = int(input('Digite a primeira nota'))
segunda = int(input('Digite a segunda nota'))
terceira = int(input('Digite a terceira nota'))
quarta = int(input('Digite a quarta nota'))

media = (primeira + segunda + terceira + quarta) / 4

print('Sua média é', media)

#5ª
metros = 1
centimetros = metros * 100
print(centimetros)
'''
# Exercicios com Arquivos

'''
#1ª
import re

arquivo = open('arquivo.txt', 'r')
resultado = arquivo.read()
lista = resultado.split('\n')
print(lista)

ip_valido = []
ip_invalido = []


for valor in lista:
    print(valor)
    padrao = valor.split('.')
    corretos = 0
    for contador in range(4):
        if int(padrao[contador]) <= 255:
            corretos = corretos + 1
            print(corretos)
            if corretos == 4:
                print('entrei aqui')
                print(valor)
                ip_valido.append(valor)
        else:
            ip_invalido.append(valor)          

print('IPs Válidos', ip_valido)
print('Invalidos', ip_invalido)

arquivo_texto = open('arquivosaida.txt', 'w')

arquivo_texto.write(u'[Endereços válidos:]' + '\n')
for item in ip_valido:
    arquivo_texto.write(item + '\n')

arquivo_texto.write(u'\n'+'[Endereços inválidos:]' + '\n')
for item in ip_invalido:
    arquivo_texto.write(item + '\n')
'''

#2ª
import re


def conversor(valor):
    mega = valor / 1000000
    return round(mega, 2)

def percentual(total_geral, total_individual):
    total_individual = float(total_individual)
    soma_total = 0
    for qtd in total_geral:
        soma_total = soma_total + qtd
    
    porcentagem = (total_individual * 100) / soma_total
    return round(porcentagem, 2)

arquivo = open('usuarios.txt', 'r')
resultado = arquivo.read()
lista = resultado.splitlines()
usuarios = []
dados = []
dados_em_string = []
porcentagem_de_uso = []

for usuario in lista:
    pesquisa_usuario = re.search(r'\w{1,15}', usuario)
    nome = pesquisa_usuario.group()
    if len(nome) < 15:
        diferenca = len(nome) + 15 - len(nome)
        nome = nome.ljust(diferenca)
    usuarios.append(nome)
    pesquisa_dados = re.search(r'\d{1,15}', usuario)
    dados.append(conversor(float(pesquisa_dados.group())))

for valor in dados:
    porcentagem_de_uso.append(percentual(dados, valor))
    if len(str(valor)) < 8:
        valor = str(valor)
        diferenca = len(valor) + 8 - len(valor)
        valor = valor.ljust(diferenca)
        dados_em_string.append(valor)
        


escrever_arquivo = open('relatório.txt', 'w')

escrever_arquivo.write('ACME Inc.                    Uso de espaço em disco pelos usários' + '\n')
escrever_arquivo.write('--------------------------------------------------------------------------------'+ '\n')
escrever_arquivo.write(r'Nr.  Usuário         Espaço utilizado           % do uso'+ '\n')
for posicao in range(len(usuarios)):
    escrever_arquivo.write(str(posicao + 1) + '   ' + usuarios[posicao] + '     ' + str(dados_em_string[posicao]) + 'MB' + '                 ' + str(porcentagem_de_uso[posicao])+'%'+ '\n')

