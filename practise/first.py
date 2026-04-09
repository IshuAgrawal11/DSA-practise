n = int(input("Enter the number of rows: "))
# num = int(n**0.5) + 1
for i in range (1, n+1):
    if i == 1:
        print(f"{i} is Neither Prime nor Composite")
    elif i == 2:
        print(f"{i} is Prime")
    elif i % 2 == 0:
            print(f"{i} is Not Prime")
    else:
        for j in range (3, int(i**0.5) + 1, 2):
            if i % j == 0:
                print(f"{i} is Not Prime")
                break
        else:
            print(f"{i} is Prime")


        
    