num = input("enter number> ")
num = int(num)
if num > 15:
     print(f"the input is more than 15")
elif num < 15:
    print(f"the input is less than 15")
elif num == 15:
    print("the input is a neutral number, that is neither more or less than 15.")
else:
    print("input is invalid.")
