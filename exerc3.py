def main():
  numPedidos = int(input("Núm de pedidos: "))
  for i in range(1, numPedidos + 1):
    prato = input("Prato: ")
    calorias = int(input("Calorias: "))
    ehVegano = input("É vegano?")

    # //TODO: Tendo em vista a variável booleana "ehVegano", imprima a saída deste desafio.
    if ehVegano == 's':
      print(f"Pedido {i}: {prato} (Vegano) - {calorias} calorias")
    elif ehVegano == 'n':
      print(f"Pedido {i}: {prato} (Nao-vegano) - {calorias} calorias")

main()