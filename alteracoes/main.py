from banco import *
from alteracoes.deposito import depositar
from alteracoes. consulta import consultarSaldo
from alteracoes.saque import sacar
from alteracoes.transferencia import transferir

def menu():
    while True:
        print('------------------ Sistema Bancário ------------------')
        print('1 - Adicionar conta')
        print('2 - Editar conta')
        print('3 - Editar conta')
        print('4 - Apagar conta')
        print('5 - Listar contas')
        print('6 - Atualizar nome')
        print('7 - Atualizar saldo')
        print('8 - Realizar saque')
        print('9 - Realizar depósito')
        print('10 - Consultar saldo')
        print('11 - Transferência')
        print("12 - Sair")
        opcao = input('Selecione uma opcão: ')
        