n=int(input())
if n%4==0:
  if n%400==0:
    print("yes")
  elif n%100!=0:
    print("yes")
  else:
    print("no")
else:
  print("no")
