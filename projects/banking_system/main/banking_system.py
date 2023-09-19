'''
Um banco deseja mordenizar suas operações e para isso escolheu a lingugagem Python. 
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito,
saque e extrato.
'''
import sys 


saldo = 1000
count = 0

def menu ():

    print("\n             SEJA BEM-VINDO\n ")
    print("    Escolha a operação que deseja realizar:\n ")
    print("         [1]-Saque      [2]-Depósito\n\n         [3]-Extrato    [4]-Sair")

    num = int(input())
   
    return num
 
count = 0
saldo = 1000
limite = 500
extrato = []
num = menu()

while True:
    
    
    if num == 1:
        saque = float(input("Digite o valor que deseja sacar: "))
        
        if count >= 3:
            print("Limite de saques excedido!")
            num
           
        elif saque <= saldo and saque <= limite:
            saldo = saldo - saque
            print("Saque realizado com sucesso!")
            count += 1
            
            extrato.append([" ",-saque, saldo])
            
            print("Seu saldo atual é de: R$", saldo)
            
        elif saque >= limite:
            print("Limite excedido!"
                  "\n""O limite de saque é de R$ 500,00")
            
        else:
            print("Saldo insuficiente!")
            print("Seu saldo atual é de: R$", saldo)
        
       
        
        num = menu()
        
    if num == 2:
        
        deposito = float(input("Digite o valor que deseja depositar: "))
        if deposito > 0:
            saldo = saldo + deposito
            print("Deposito realizado com sucesso!")
           
            extrato.append([deposito," " , saldo])
            print("Seu saldo atual é de: R$", saldo)
            
        else:
            print("Valor inválido! ")
            
            
        
        
        num = menu()
        
    if num == 3:
        
        print(f"------------ Extrato---------------------""\n")
        print(f"                    Saldo Atual R${saldo}""\n")
        print(f" Credito     Debito      Saldo ")
        for e in extrato:
            print(f"-----------------------------------------""\n")
            print(f"  {e[0]}          {e[1]}       {e[2]}")
        
        num = menu()
        
    if num == 4:
        print("Obrigado por utilizar nossos serviços!")
        sys.exit()
        
    

