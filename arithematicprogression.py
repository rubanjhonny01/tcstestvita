nn,a,d=map(int,input().split())
ap=a
for i in range(nn-1):
  a=a+d
  ap+=a
print(ap)
