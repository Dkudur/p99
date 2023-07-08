
name = input("Enter your name: ")
iteration = len(name)

for i in range(0, iteration):
    for j in range(0, iteration):
        if j == i:
            print (name[j], sep = " ", end = " ")
        elif j != i:
            print("*", end = " ")
    print()