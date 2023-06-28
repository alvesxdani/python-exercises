saldo = float(0)
TOTAL_SAQUES = 0
operacao = int(input("""
Qual operação será realizada?
[0] Saque
[1] Depósito
[2] Sair
"""))



while operacao != 2:
    if operacao == 0 and TOTAL_SAQUES < 3:
        valor = float(input("Quantidade a sacar: "))
        saldo = saldo - valor
        TOTAL_SAQUES = TOTAL_SAQUES + 1
        print(f"Seu saldo atual é: R$ {saldo : .2f}")

    elif operacao == 0 and TOTAL_SAQUES <= 3:
        print('Você atingiu o limite de saques diários (3 saques por dia)')

    elif operacao == 1:
        valor = float(input("Quantidade a depositar: "))
        saldo = valor + saldo
        print(f"Seu saldo atual é: R$ {saldo : .2f}")

    else:
        operacao = int(input("Operação desconhecida. Digite novamente: "))

    operacao = int(input("Digite o número da nova operação: "))
    
