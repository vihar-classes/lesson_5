num = int(input("Enter a positive integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    result = 1
    for i in range(1, num + 1):
        result = result * i
    print(f"The factorial of {num} is {result}")