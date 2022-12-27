# Can also use eval():
# math = input("Expression: ").strip().replace(" ", "")
# print(float(eval(math)))

math = input("Expression: ").strip()
x, y, z = math.split(" ")

num1 = float(x)
num2 = float(z)

if y == "+":
    result = num1+num2
    print(f"{result:.1f}")
elif y == "-":
    result = num1-num2
    print(f"{result:.1f}")
elif y == "*":
    result = num1*num2
    print(f"{result:.1f}")
elif y == "/":
    result = num1/num2
    print(f"{result:.1f}")