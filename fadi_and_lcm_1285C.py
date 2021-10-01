import math
x=int(input())


z=1
for i in range(1,int(math.sqrt(x))+1):

    if(x%i==0 and math.gcd(i,x//i)==1):
        z=i

print(z,x//z)
        
