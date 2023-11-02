while True:
    a = input("Введіть додатне число a: ")
    b = input("Введіть додатне число b: ")

    try:
        a = int(a)
        b = int(b)

        if a > 0 and b > 0:
            if a > b:
                x = a/b - 1
            elif a == b:
                x = -25
            elif a < b:
                x = (a**3 - 5) / a
            print("Результат:", x)
            break
        else:
            print("Ви ввели не додатне число")
    except ValueError:
        print("Ви ввели не число")


