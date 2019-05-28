import string
n=input()
l=string.ascii_uppercase+string.ascii_lowercase
l1=['a','e','i','o','u','A','E','I','O','U']
if n in l and n in l1:
  print("Vowel")
elif n in l and n not in l1:
  print("Consonant")
else:
  print("Invalid")
