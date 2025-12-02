name = input("whats your name? ")

if name == "vihar":
    print("allowed!")
    allowed = True
else:
    print("Get Out!")
    allowed = False
    
print(f"ARE YOU ALLOWED?: "{str(allowed)})