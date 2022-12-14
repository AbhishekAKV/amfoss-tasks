#Count number of zeroes after first non zero number
#Total = number of zeroes + sum of non-zero numbers except last number

for i in range(int(input())):
    n = int(input())
    listtanks = input().split()        #taking input for each test case
    

    l1 = []
    s = 0
    
    for i in range(len(listtanks)):      
        if listtanks[i] != '0':            #finding first non zero element in the list
            index = i
            break

    for x in range(index, len(listtanks)-1):
        l1.append(listtanks[x])           #appending all elements, starting from index into l1
    
    for j in l1:
        s += int(j)                           
    
    print(s + l1.count('0'))    
