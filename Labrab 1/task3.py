n = int(input("Введіть ціле число N (1 < N < 9): "))

for i in range(1, n + 1):
    num = n
    for j in range(1, i + 1):
        print(num, end=" ")
        num -= 1
    print("")
