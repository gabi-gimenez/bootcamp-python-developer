import sys

month = int(input())
  
month_num = list(range(1,13))

if month not in month_num:
    print("Valor Inválido!")
    sys.exit()

month_num = [str(n) for n in month_num]

month_name = ["January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]
    
    
months_dict = dict(zip(month_num,month_name))

for k,v in months_dict.items():
    if str(month) == k:
        print(v)
        
   