a = int(input("Enter the Budget you have: "))
b = int(input("Enter the price of the apple: "))
c = int(input("Enter the price of the mango: "))
if a -(b+c) >= 20:
  print("You can buy both apple and mango")
elif a - (b + c) <= 10 and a - (b + c) ==1 :
  print("You can buy half KG of apple and half KG of mango")
else:
  print("Buy nothing")
