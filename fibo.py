def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return f(n - 1) + f(n - 2)

def g():
    while True:
        try:
            n = int(input("number: "))
            if n < 1:
                print("error")
                continue
            break
        except:
            print("error")
            continue

    r = []
    for i in range(n):
        r.append(str(f(i)))
    
    print(", ".join(r))

g()
