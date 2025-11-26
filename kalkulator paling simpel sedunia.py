num1 = float(input("nomor pertama: "))
op = input("Operator (+ - * /): ")
num2 = float(input("nomor kedua: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: division by zero")
else:
    print("Invalid operator")
