n,k=map(int,input().split())
l=[]
for i in range(n,k+1):
    if i%2!=0 and i!=1:
        l.append(i)
for x in l:
    print(x,end=" ")
