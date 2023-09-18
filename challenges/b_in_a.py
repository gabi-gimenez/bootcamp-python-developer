'''
DESAFIO:
Paulinho tem em suas mãos um novo problema.
Agora a sua professora lhe pediu que construísse 
um programa para verificar, à partir de dois valores
muito grandes A e B, se B corresponde aos últimos dígitos de A.

ENTRDA:
A entrada consiste de vários casos de teste. A primeira 
linha de entrada contém um inteiro N que indica a quantidade
de casos de teste. Cada caso de teste consiste de dois
valores A e B maiores que zero, cada um deles podendo 
ter até 1000 dígitos.

'''
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
     
    