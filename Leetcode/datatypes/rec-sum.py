def add_num(x, y):
    if y == 0:
       return x
    else:
       return add_num(x + 1, y - 1)
   
num1 = input()
num2 =input()

result = add_num(num1, num2)

print("The sum of", num1, "and", num2, "is", result)
   