text = input("Input: ")
vowels = ["a", "e", "i", "o", "u"]
output = print("Output: ", end="")

for c in text:
    if c.casefold() not in vowels:
        print(c, end="")
        
print()