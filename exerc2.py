import textwrap
# MELHORANDO O CÓDIGO E FUNÇÕES
def menu():
    menu = """
    ======== MENU ========
    Qual operação será realizada?
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Cadastrar novo usuário
    [5] Criar conta
    [6] Listar usuários
    [0] Sair
    """
    return int(input(textwrap.dedent(menu)))

# Functions
def depositar(saldo, valor, extrato, /):
   if valor > 0:
      saldo += valor
      extrato += f"Depósito \tR$ {valor: .2f}\n"
      print("Depósito realizado com sucesso.")
   else:
      print("Operação inválida. Digite um valor maior que 0.")
   return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
   excedeu_saldo = valor > saldo
   excedeu_limite = valor > limite
   excedeu_saques = numero_saques >= limite_saques
   if excedeu_saldo:
      print("\n Essa operação falhou! Você não tem saldo suficiente.")
   elif excedeu_limite:
      print("\n Operação falhou! O valor do saque excede o limite.")
   elif excedeu_saques:
      print("\n Operação falhou! Número máximo de saques excedido.")
   elif valor > 0:
      saldo -= valor
      extrato += f"Saque:\t\tR$ {valor: .2f}\n"
      numero_saques += 1
      print("\n Saque realizado com sucesso!")
   else:
      print("\n Operação falhou! O valor informado é inválido.")
   return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
   print("\n ##### EXTRATO #####")
   print(f"Não foram realizadas movimentações" if not extrato else extrato)
   print(f"Seu saldo é de: {saldo : .2f}")

def criar_usuario(usuarios):
   cpf = int(input('Informe o CPF (apenas números): '))
   usuario = filtrar_usuarios(cpf, usuarios)
   
   if usuario:
      print('\n Já existe um usuário com este CPF!')
      return

   nome = input('Informe o nome completo: ')
   data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
   usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf})
   print("Usuário criado com sucesso.")

def filtrar_usuarios(cpf, usuarios):
   usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
   return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
   cpf = int(input("Informe o CPF do usuário: "))
   usuario = filtrar_usuarios(cpf, usuarios)

   if usuario:
      print("\n Conta criada com sucesso")
      return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
   
   print("\n Usuário não encontrado, fluxo de criação de conta encerrado.")

def listar_contas(contas):
   for conta in contas:
      linha = f"""
      Agência: \t\t{conta["agencia"]}
      C/C: \t\t{conta["numero_conta"]}
      Titular: \t\t{conta["usuario"]["nome"]}
      CPF: \t\t{conta["usuario"]["cpf"]}
      """
      print(linha)
   if not contas:
      print("Não há contas cadastradas.")

# program
def main():
   LIMITE_SAQUES = 3
   AGENCIA = "0001"

   saldo = 0
   limite = 500
   extrato = ""
   numero_saques = 0
   usuarios = []
   contas = []

   while True:
      opcao = menu()

      if opcao == 1:
         valor = float(input("Informe o valor do depósito: "))
         saldo, extrato = depositar(saldo, valor, extrato)
      
      elif opcao == 2:
         valor = float(input("Informe o valor do saque: "))
         saldo, extrato = sacar(
         saldo=saldo,
         valor=valor,
         extrato=extrato,
         limite=limite,
         numero_saques=numero_saques,
         limite_saques=LIMITE_SAQUES,
         )
      
      elif opcao == 3:
        exibir_extrato(saldo, extrato=extrato)
        
      elif opcao == 4:
        criar_usuario(usuarios)
        
      elif opcao == 5:
         numero_conta = len(contas) + 1
         conta = criar_conta(AGENCIA, numero_conta, usuarios)
         if conta:
            contas.append(conta)
      
      elif opcao == 6:
         listar_contas(contas)
         
      elif opcao == 0:
         break

      else:
         opcao = int(input("Operação inválida. Digite a opção novamente: "))

main()