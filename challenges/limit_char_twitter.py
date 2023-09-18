'''
DESAFIO:
O microblog Twitter é conhecido por limitar as 
postagens em 140 caracteres. Conferir se um texto
vai caber em um tuíte é sua tarefa.

'''

T = input()
    
T_list = []

for l in str(T):
    
    T_list.append(l)
    
    
if  len(T_list) <= 140:
    print("TWEET")  
    
else:
    print("MUTE")  


     
        

            
    
