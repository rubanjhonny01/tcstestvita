n,k=map(int,input().split())
l=[]
for i in range(n,k):
    if i%2==0:
        l.append(i)
for x in l:
    print(x,end=" ")
