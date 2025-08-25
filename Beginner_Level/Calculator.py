print("Operations")
print("1.Addition")
print("2.Multiplication")
print("3.Division")
print("4.Substraction")

print("Enter the two number you want")

num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))

oper = int(input("Please enter the Operation (1,2,3,4)"))

match oper :
  case 1:
    print("Addition")
    print("The answer is :", num1+num2)
  case 2:
    print("Multiplication")
    print("The answer is :",num1*num2)
  case 3:
    print("Division")
    print("The answer is :" , num1/num2)
  case 4 :
    print("Substarction")
    print("The answer is:", num1-num2)
  case _ :
    print("Invalid Option")
    print("Please follow the instructions")
