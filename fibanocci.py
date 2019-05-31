n=int(input())
a=0
b=1
for i in range(n):
  fact=a+b
  a=b
  b=fact
print(fact)
