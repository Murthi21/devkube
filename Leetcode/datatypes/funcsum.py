def add(a,b):
    return a+b


num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = int(num1) 
num2 = int(num2)

sum_result = add(num1,num2)

print("sum of ", num1, "and", num2, "is", sum_result)