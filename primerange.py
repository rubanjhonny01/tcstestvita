nn,k=map(int,input().split())
l=[]
for i in range(nn+1,k):
  count1=0
  for j in range(1,i):
    if i%j==0:
      count1+=1
  if count1==1:
    l.append(i)
for x in l:
  print(x,end=" ")
