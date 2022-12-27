answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

right = ["42", "forty two", "forty-two"]

if answer in right:
    print("Yes")
else:
    print("No")