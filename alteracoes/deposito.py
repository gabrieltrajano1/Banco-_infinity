from banco import banco, obterConta

def depositar(conta:int, valor:float) -> bool:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] += valor
        print('Valor depositado com sucesso!')
    else:
        print('Cliente não encontrado com sucesso')


depositar( 5, 5000)
print(banco)