operator = input("donnee une operation + - * / : ")
num1 = float(input("donnee num1 : " ))
num2 = float(input("donnee num2 : " ))
if operator == "+":
    print(f"the result is {num1 + num2}")
elif operator == "-":
    print(f"the result is {num1 - num2}")
elif operator == "*":
    print(f"the result is {num1 * num2}")
elif operator == "/":
    print(f"the result is {num1 / num2}")