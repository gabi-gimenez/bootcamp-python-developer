N = int(input())

n = 0

while(n < N):

    A = int(input("Digite A: "))
    B = int(input("Digite B: "))

    if A > 0 and B > 0:
        A = [a for a in str(A)]
        
        
        B = [b for b in str(B)]

        
        if len(A) and len(B) <= 1000:
            
            if B == A[-len(B):]:
                print("Encaixa")

            else:
                print("Não Encaixa")

            n = n + 1
            

        else:
            print("Valor inválido!")
            break 
    else:
        print("Valor inválido!")
     
    