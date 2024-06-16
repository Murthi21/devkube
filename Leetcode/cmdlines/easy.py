# Create a list of your favorite fruits.
# Access the second element of the list.
# Add a new fruit to the end of the list.
# Remove the first element of the list.
# Check if a specific fruit is in the list.
# Print the length of the list.
# Reverse the order of the elements in the list.
# Sort the elements of the list in alphabetical order.
# Create a new list by concatenating two existing lists.
# Create a slice of the list containing only the first three elements.


x=["Apple", "Banana","Orange","Guva"]

print(x)

print("Second element of list",x[1])

x. append("fruit1")
print("append the new fruit in list",x)
x.remove("Apple")
print("removed the first index",x)
    
print("Lenght of list",len(x))

print("Reverse string")
print(x[::-1])

print("sorted lsit")
x.sort()
print(x)

# Create a new list by concatenating two existing lists.
# Create a slice of the list containing only the first three elements.

y=["f1","f2"]
l=x + y 
print(l)

print(l[0:3])

      
