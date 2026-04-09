n = int(input("Enter the number: "))
ans = 1
found = False
while ans <= n:
    if ans == n:
        print("true")
        found = True
        break
    ans  = ans * 2

if not found:
    print("false")