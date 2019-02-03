'''
AULA 5
quantidade_pessoas = input('Quantas pessoas serão convidadas?')
lista_convidados = []

for item in range(int(quantidade_pessoas)):
    lista_convidados.append(input('Qual o nome do convidado?'))

print(lista_convidados)
'''

'''
AULA 6
minha_lista = ['Adson', 'Jose']  # LISTA (list)
minha_tupla = ('Adson', 'Joao')  # TUPLA (tuple) não pode alterar a quantidade de itens, necessário substituir toda a tupla para funcionar ESTATICO
meu_dicionario = {'nome': 'Guilherme', 'idade':27} # DICIONARIO (dict) funciona como um json, passando as informações de algo, não tem INDICE, tem CHAVE
meu_conjunto = {'Gui', 'Joao'} # CONJUNTO (set) não pode ter itens iguais, funciona como a lista, não tem INDICE, transforma em tabela HASH, deixando a pesquisa extremamente rapida

# Declarando vazio
lista = []
tupla = ()
dicionario = {}
conjunto = set()

if 'Guilherme' in meu_dicionario.values():
    print('Está aqui')
'''

'''
AULA 7
def soma(numero1, numero2):  #Modo de criar uma função em Python
    resp = numero1 + numero2
    return resp

print(soma('Oi ','Tudo bom'))

lista_numeros = [3,6,2,1,8,7,5,10,12,15,4]

def maior_valor(lista):
    numero_maior = 0
    for valor in lista_numeros:
        if valor >= numero_maior:
            numero_maior = valor
    return numero_maior

print(maior_valor(lista_numeros))
'''

'''
AULA 8
import sys

argumentos = sys.argv # arg1 method // arg 2 - n1 // arg3 - n2

def soma(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

if argumentos[1] == "soma":
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    resp = sub(float(argumentos[2]), float(argumentos[3]))

print(resp)
'''

'''
AULA 9
#Criando uma classe para ser usada em OO
class Veiculo:
    def __init__(self, cor, rodas):
        self.cor = cor
        self.rodas = rodas

#Como seria o import de uma classe para outro arquivo
#from veiculo import Veiculo

#Trabalhando com herança, carro terá as mesmas caracteristicas de Veiculo
class Carro(Veiculo):
    def __init__(self, cor, rodas):
        Veiculo.__init__(self, cor, 4)
'''

'''
AULA 10
#o 'w' serve para escrever ou criar um arquivo, o 'r' é somente para leitura, o 'r+' é tanto para leitura quanto escrita mas da prioridade para leitura e o 'a' serve para adicionar algo em um arquivo, funciona para criar também, quando não for arquivos de texto, suar o b de bytes
arquivo = open('arquivo.txt', 'w') 
arquivo.write('Olar pessoas')
'''
'''
AULA 11
import time

def abre_arquivo():
    try:
        arquivo = open('arquivodoido.txt')
        return True
    except Exception as erro:
        print('Aconteceu algum erro:', erro)
        return False

while not abre_arquivo():
    print('Tentando abrir o arquivo')
    time.sleep(5)

print ('Consegui abrir o arquivo')
'''
'''
AULA 12
import requests #Beautiul Code 4 (pesquisar depois)

requisicao = requests.get('https://solyd.com.br/')

print(requisicao.text)
'''

'''
AULA 13 OMDB Filmes
import requests
import json

req = requests.get('http://www.omdbapi.com/?t=the+punisher')

print(req)
'''

#AULA 14 Expressões regulares
import re

string_de_teste = 'O gato é bonito gatawaw gatussss gatigr'

padrao = re.search(r'gat.', string_de_teste) #o 'r' ou RAW string no inicio serve para tirar a função de caracteres especiais dentro da string tal como um /n. o Ponto no final signifca qualquer caractere que vem, \w significa letra
padrao_find = re.findall(r'gat\w', string_de_teste)
padrao_tudo = re.findall(r'gat\w+', string_de_teste)

if padrao:
    print(padrao.group())
else:
    print("Padrao não encontrado")

if padrao_find:
    print(padrao_find)
else:
    print("Padrao não encontrado")

if padrao_tudo:
    print(padrao_tudo)
else:
    print("Padrao não encontrado")