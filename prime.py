n=int(input())
count1=0
for i in range(n):
  if n%i==0:
    count1+=1
if count1==1:
  print("yes")
else:
  print("no")
