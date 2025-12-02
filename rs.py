try:
    cp = float(input("Enter the cost price (CP) in rupees: "))
    sp = float(input("Enter the selling price (SP) in rupees: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

diff = sp - cp

if diff > 0:
    p = diff
    print(f"\nResult: Profit!")
    print(f"The person has a profit of {p:.2f} rs.")
elif diff < 0:
    l = abs(diff)
    print(f"\nResult: Loss!")
    print(f"The person has a loss of {l:.2f} rs.")
else:
    print(f"\nResult: No Profit, No Loss.")
    print("The selling price is equal to the cost price.")
