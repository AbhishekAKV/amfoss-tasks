#input - n as predicted amount, m as the amount of money with joe
(n, m) = map(int, input().split())

#t1 - amount of money/predicted amount
t1 = m/n

#t - remainder when m divided by n
t = m%n


#if amount of money not divisible by predicted amount, it isn't possible 
if t != 0:
    print(-1)
    
elif t1 == 1:      #zero steps if the amount of money is already equal to predicted amount
    print(0)

elif n>m:           #not possible of predicted amount greater than money with joe because money can only decrease
    print(-1)
    
elif t == 0 and (t1%3==0 or t1%2==0):
    n = 0                               #if divisible and the quotient of m/n divisible by 3 or 2
    while t1 != 1:
        if t1%3 == 0:                               
            t1 = t1/3  #dividing by 3 because money becomes 1/3rd    #counting number of steps, incrementing by 1
            n+=1
        else:
            t1 = t1/2   #dividing by 2 when not divisible by 3(other table)
            n += 1
    print(n)
