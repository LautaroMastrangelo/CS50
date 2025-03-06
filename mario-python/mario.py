from cs50 import get_int

while (1):
    height = get_int("height: ")
    if (height > 0 and height < 9):
        break
for i in range(1, height+1):
    print(" " * (height - i), end="")
    for j in range(2):
        print("#" * i, end="")
        if j == 0:
            print("  ", end="")
    print()
