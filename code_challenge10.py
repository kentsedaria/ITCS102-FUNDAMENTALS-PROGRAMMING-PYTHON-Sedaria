print("\t\t", end=" *")
for i in range(1, 11):
    for x in range(10, i, -1):
        print(" ", end=" ")
    for y in range(1, i):
        print("*", end=" ")
    for z in range(1, i):
        print("*", end=" ")
    print()