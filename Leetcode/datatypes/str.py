##Concatentaion
str1 = "something"
str2 = "attached"

print(str1  +"", str2)
print(len(str1))

## Lowercase
text = "To be changed"
u=text.upper()
l=text.lower()
print("Uppercase", u)
print(" Lowercase", l)

#String replace

new_text = text.replace("changed", "Done")
print("Modofied Text", new_text)

##Spilt function
print(text.split())

##Strip
stripped_text = text.strip()
print("Stripped text:", stripped_text)

substring = "is"
if substring in text:
    print(substring, "found in the text")
