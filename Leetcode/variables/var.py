y = 20  # Global variable

def another_function():
    print("sample print", y)
    add = y + 5
    print("addition from function", add)      # This will access the global variable 'y'

another_function()
print(y)  # This will print 20