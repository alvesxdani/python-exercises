# MELHORANDO O CÓDIGO E FUNÇÕES

saldo = float(0)
EXTRATO_OPS = []
TOTAL_SAQUES = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"

operacao = int(input("""
======== MENU ========
Qual operação será realizada?
[1] Saque
[2] Depósito
[3] Extrato
[4] Cadastrar novo usuário
[5] Sair
"""))

# Functions
def saque(valor):
    global saldo
    global TOTAL_SAQUES
    global EXTRATO_OPS
    if valor > 0:
        saldo -= valor
        print("Saque realizado com sucesso.")
    else:
        print("Operação inválida. Digite um valor maior que 0.")
    print(f"Seu saldo atual é: R$ {saldo : .2f} \n")
    print(f"Este é seu {TOTAL_SAQUES}º saque.")
    TOTAL_SAQUES = TOTAL_SAQUES + 1
    EXTRATO_OPS.append({"valor": valor, "tipo_ops": "Saque"})

def deposito(valor):
    global saldo
    global EXTRATO_OPS
    if valor > 0:
        saldo += valor
        print("Depósito realizado com sucesso.")
    else:
        print("Operação inválida. Digite um valor maior que 0.")
    print(f"Seu saldo é de: {saldo : .2f}")
    EXTRATO_OPS.append({"valor": valor, "tipo_ops": "Depósito"})

def extrato():
    global saldo
    global EXTRATO_OPS
    print("\n ##### SEU EXTRATO #####")
    print(f"Seu saldo é de: {saldo : .2f}")

# program
while operacao != 5:
    if operacao == 1 and TOTAL_SAQUES < LIMITE_SAQUES:
     valor = float(input("Quantidade a sacar: "))
     saque(valor)
    
    elif operacao == 0 and TOTAL_SAQUES <= LIMITE_SAQUES:
        print('Você atingiu o limite de saques diários (3 saques por dia)')

    elif operacao == 2:
        valor = float(input("Quantidade a depositar: "))
        deposito(valor)
    
    elif operacao == 3:
        extrato()

    else:
        operacao = int(input("Operação desconhecida. Digite novamente: "))

    operacao = int(input("Digite o número da nova operação: "))