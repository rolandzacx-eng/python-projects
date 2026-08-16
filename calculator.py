def add (a, b):
     return a + b
def subtract (a, b):
     return a - b
def multiply (a, b):
     return a * b
def divide (a, b):
     return a / b
def power (a, b):
     return a ** b
def modulus (a, b):
     return a % b

operations = {
     "+": add,
     "-": subtract,
     "*": multiply,
     "/": divide,
     "**": modulus,
     "%": modulus
}
     
print("Simple calculator")
print("Operations: + - * /  (type q to quit)")

while True:
   operation = input("Enter operation: ")

   if operation == "q":
      print("Goodbye!")
      break
   try:
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
   except ValueError:
       print("Error: please enter valid numbers")
       continue
   if operation in operations:
       try:
           print(operations[operation](num1,num2))
       except ZeroDivisionError:
           print("Error: cannot divide by zero")
   else:
       print("invalid operation")




