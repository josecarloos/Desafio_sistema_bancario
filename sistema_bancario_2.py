import textwrap


def menu():
     menu = '''\n
=========== MENU ===========    

[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova conta
[lc]\tlistar contas
[nu]\tNovo usuário
[m]\tMostrar meus dados
[q]\tSair
==>'''
     return input(textwrap.dedent(menu))
def saque(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
     excedeu_saldo = valor > saldo
     excedeu_limite = valor> limite
     excedeu_saques = numero_saques > limite_saques

     if excedeu_saldo:
          print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
     
     elif excedeu_limite:
          print("\n@@@ Operação falhou! Valor do saque excede o limite. @@@")

     elif excedeu_saques:
          print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

     elif valor > 0:
          saldo -= valor
          extrato += f"Saque:\t\tR$ {valor:.2f}\n"
          numero_saques += 1
          print("\n === Saque realizado com sucesso! ===")
     
     else:
          print("@@@ Operação falhou! O valor informado é invalido.@@@")
          
     return saldo,extrato
def deposito(saldo, valor, extrato, /):  
     if valor > 0:
          saldo += valor
          extrato += f"Depósito:\tR$ {valor:.2f}\n"
          print("\n=== Depósito realizado com sucesso! ===")
     else:
          print("\n@@@ Operação falhou! O valor informado é invalido. @@@")

     return saldo, extrato
def exibir_extrato(saldo,/,*,extrato):

     print("\n================ EXTRATO ================")
     print("Não foram realizadas movimentações" if not extrato else extrato)
     print(f"\nSaldo:\t\tR$ {saldo:.2f}")
     print("=========================================")
def criar_usuario(usuarios):
     cpf= input("Informe o seu CPF(somente números): ")
     usuario = filtrar_usuario(cpf, usuarios)
     if usuario:
          print("\n@@@ Já existe usuário com esse CPF! @@@")
          return
     
     nome = input("Informe seu nome completo: ")
     data_nascimento = input("Informe sua data de nascimento(DD/MM/AAAA): ")
     endereco = input("Informe seu endereço (Logradouro,numero,bairro,cidade,sigla/estado): ")
     usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf" : cpf, "endereco":endereco})
     print("=== Usuário craido com sucesso! ===")
def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(agencia,numero_conta,usuarios):

     cpf = input("Informe o seu CPF de usuário: ")
     usuario = filtrar_usuario(cpf,usuarios)

     if usuario:
          print("\n === Conta criada com sucesso! ===")
          return{"agencia": agencia, "numero_conta": numero_conta,"usuario":usuario}
     print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrada! @@@")
def listar_contas(contas):
     for conta in contas:
          linha =f"""\
          Agência:\t{conta['agencia']}
          C/C:\t\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['nome']}
          """
          print("=" * 100)
          print(textwrap.dedent(linha))

def main():
     LIMITE_SAQUES = 3
     AGENCIA = "0001"

     extrato = ""
     numero_saques = 0
     saldo = 0
     limite = 500
     usuarios = []
     contas = []


     while True:
          opcao = menu()
     
          if opcao == "d":
               valor = float(input("\nInforme o valor que Sr(a) gostaria de depositar: "))
               
               saldo, extrato = deposito(saldo, valor, extrato)
                         
          elif opcao == "s":
               valor = float(input("Informe o valor que o Sr(a) gostaria de sacar:"))
               
               saldo,extrato = saque(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite= limite,
                    numero_saques=numero_saques,
                    limite_saques= LIMITE_SAQUES,
               )             
          elif opcao =="nu":
               criar_usuario(usuarios)
          
          elif opcao == "nc":
               numero_conta =len(contas) +1
               conta = criar_conta(AGENCIA,numero_conta,usuarios)
               if conta:
                    contas.append(conta)
          elif opcao =="lc":
               listar_contas(contas)

          elif opcao == "e":
               exibir_extrato(saldo,extrato=extrato)
     
          elif opcao == "q":
               break 
          
          else:
               print("\nOperação incorreta, Tente novamente!")

main()
