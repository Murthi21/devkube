# Write a function that takes a list of numbers and returns the sum of all the even numbers.


def even_add(num):
    sum_e = 0
    for x in num:
        if x % 2 == 0:
            sum_e += x
    return sum_e

num = [1,2,3,4,5,6]

print(even_add(num))

#Uppercase
# Write a function that takes a list of strings and returns a new list with all the strings in uppercase.

#u=text.upper()
def upperCase(lc):
    newl=[]
    for x in lc:
        newl.append(x.upper())
    return newl

lc = ["a","b","c"]
print(lc)
print(upperCase(lc))
   
# Write a function that takes a list of words and returns a new list with all the words that are longer than 5 characters.

def longerthan5(str):
    new=[]
    for x in str:
        if len(x) >= 5:
            new.append(x)
    return new


str = ["abc","abcd","abcdef"]
print(longerthan5(str))


# Write a function that takes a list of numbers and returns the largest number in the list.

def largest_number(numbers):
    large = numbers[0]
    for x in numbers:
        if x > large:
            large = x
    return large        

 
numbers = [3, 41, 12, 9, 74, 15]
print(largest_number(numbers))

# Write a function that takes a list of numbers and returns the average of all the numbers.
def avg_num(numbers):
    sum_numbers = sum(numbers)
    average = sum_numbers / len(numbers)
    return average

print(avg_num(numbers))    