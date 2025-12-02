num = input("enter number> ")
num = int(num)
if num > 0:
     print(f"the input is a positive number!")
elif num < 0:
    print(f"the input is a negative number")
elif num == 0:
    print("the input is a neutral number, that is neither positive or negative. Ask Google for more info.")
else:
    print("input is invalid.")