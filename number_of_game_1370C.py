t=int(input())

import math

def isPrime(n):


    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return 0
    return 1
for _ in range(t):

    n=int(input())

    s1="Ashishgup"
    s2="FastestFinger"


    if(n==1):
        print(s2)

    elif(n==2):
        print(s1)

    elif(n>2 and n%2==1):
        print(s1)

    else:

        if(n&(n-1)==0):
            print(s2)

        elif(n%4==0):
            print(s1)
        elif(isPrime(n//2)):
            print(s2)
        else:
            print(s1)
            
    
