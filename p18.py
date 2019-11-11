a = int(input("First number:"))
b = int(input("Second number:"))
c = int(input("Third number:"))
if a > b and a > c:
  print("The biggest is "+str(a))
elif b > c and b > a:
  print("The biggest is "+str(b))
else:
  print("The biggest is "+str(c))