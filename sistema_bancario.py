menu ='''
-----------------------------          
    [d] - DEPÓSITO
    [s] - SAQUE
    [e] - EXTRATO
    [q] - SAIR
---------------------------- 
==>'''

extrato = ""
saque_diario = 0
saldo = 0
LIMITE_SAQUE = 3


while True:

    opcao = input(menu)
    
    if opcao == "d":

        valor_deposito = float(input("\nInforme o valor que Sr(a) gostaria de depositar: "))
        
        if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f'Depósito: R${valor_deposito:.2f}\n'
                print("\nDepositando...")
        else:
             print("Valor incorreto para depósito!")
                
    elif opcao == "s":
         valor_saque = float(input("Informe o valor que o Sr(a) gostaria de sacar:"))
         
         if LIMITE_SAQUE > saque_diario and valor_saque <= 500 and saldo >= valor_saque >= 0:
              print("\nSacando...")
              saque_diario += 1
              saldo -=valor_saque
              extrato += f'Saque: R${valor_saque:.2f}\n'
         elif valor_saque <= 0:
              print("\nValor incorreto para saque!")
         elif valor_saque > 500:
              print("\nValor de saque acima do limite!")
         elif saldo < valor_saque:
              print("\nSaldo insuficiente...")
         else:
              print("\nLimite de saque diarios atingido")
         
    
    elif opcao == "e":
        print('==============EXTRATO===============\n')
        print("Não foram realizados movimentações" if not extrato else extrato)
        print(f'Seu saldo atual é: R${saldo:.2f}')
        print('==============EXTRATO===============')

    elif opcao == "q":
            print("Você saiu do menu do banco!\n")
            break
    else:
         print("\nOperação incorreta, Tente novamente!")




