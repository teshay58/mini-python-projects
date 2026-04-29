
while True:
    size = int(input("Enter the size of diamond: \n> "))
    inner = input("With internal or not (y/n): \n> ")

    print(" " * size,end="")
    print("/\\")
    j = 2
    for i in reversed(range(1,size)):
        print(" " * i,end="")
        print("/",end="")
        if inner == "y":
            for k in range(size-i):
                print("/",end="")
            for k in range(size-i):
                print("\\",end="")
        else:
            print(" " * j, end="")
        print("\\")
        j += 2
    j-=2
    for i in range(1,size):
        print(" " * i,end="")
        print("\\",end="")
        if inner == "y":
            for k in range(size-i):
                print("\\",end="")
            for k in range(size -i):
                print("/",end="")
        else:
            print(" " * j, end="")
        print("/")
        j -= 2
    print(" " * size,end="")
    print("\\/")
