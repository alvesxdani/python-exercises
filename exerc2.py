# MELHORANDO O CÓDIGO E FUNÇÕES
def menu():
    menu = int(input("""
    ======== MENU ========
    Qual operação será realizada?
    [1] Saque
    [2] Depósito
    [3] Extrato
    [4] Cadastrar novo usuário
    [5] Filtrar usuários
    [0] Sair
    """))
    return menu

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

def criar_usuario(usuarios):
   cpf = int(input('Informe o CPF (apenas números): '))
   usuario = filtrar_usuarios(cpf, usuarios)

   if usuario:
      print('\n Já existe um usuário com este CPF!')

   nome = input('Informe o nome completo: ')
   data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
  
   usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf})

def filtrar_usuarios(cpf, usuarios):
   usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
   return usuarios_filtrados[0] if usuarios_filtrados else None
   



# program
def main():
   saldo = float(0)
   EXTRATO_OPS = []
   TOTAL_SAQUES = 0
   LIMITE_SAQUES = 3
   USUARIOS = []
   CONTAS = []

   operacao = menu()
   
   while operacao != 0:
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

     elif operacao == 4:
        criar_usuario(USUARIOS)

     elif operacao == 5:
        cpf = input('Digite o CPF: ')
        filtrar_usuarios(cpf, USUARIOS)
     
     else:
        operacao = int(input("Operação desconhecida. Digite novamente: "))
     
     operacao = int(input("Digite o número da nova operação: "))

main()