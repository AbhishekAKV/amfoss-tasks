t = int(input())
for i in range(t):
    n = int(input())
    heroes = input().split() #levels of the heroes in a list
    
    more_than_one = False
    for j in heroes:
        if heroes.count(j) > 1:
            more_than_one = True
            break 
        else:
            continue
                 
    if '0' in heroes:
        print(n - heroes.count('0'))  #IF 1 or more zeroes in list each hero can be debuffed with the zero
    
    elif more_than_one == True:         #NO zeroes and similar hero levels
        print(n)
        
    else:
        print(n+1)                #NO zeroes and NO similar hero levels
