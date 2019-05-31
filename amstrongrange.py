nn,kn=map(str,input().split())
l=[]
for n in range(int(nn)+1,int(kn)):
  s=0
  i=len(str(n))
  for x in str(n):
    s=s+int(x)**i
  if str(s)==str(n):
    l.append(n)
for x in l:
  print(x,end=" ")
