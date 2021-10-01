d={}

s=input()

for i in range(len(s)):

    d[s[i]]=1+d.get(s[i],0)


odd=0

for key in d:

    if(d[key]&1):
        odd+=1

if(odd==0 or (odd&1)):
    print("First")
else:
    print("Second")
