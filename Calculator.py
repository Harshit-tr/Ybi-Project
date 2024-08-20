A = "Calculater"
print(A)
x = input("Enter your first number: ")
y = input("Enter your second number: ")
z = input("Choose  your operation +,-,*,/: ")
match z:
 case "+":
  print(int(x) + int(y))
 case "-":
   print(int(x) - int(y))

 case "*":
   print(int(x) * int(y))
 case "/":
   print(int(x) / int(y))