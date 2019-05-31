n,k=map(int,input().split())
l=[]
for i in range(n+1,k+1):
    if i%2==0:
        l.append(i)
for x in l:
    print(x,end=" ")
