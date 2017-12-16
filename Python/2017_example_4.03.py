def draw_7():
    for x in range(7):
        for y in range(7):
            print(" *", end="")
        print()


def stars_and_stripes():
    for x in range(6):
        for y in range(7):
            if x % 2 == 0:
                print(" *", end="")
            else:
                print(" -", end="")
        print()


def increasing_triangle():
    for x in range(2, 9):
        for y in range(1, x):
            print(" " + str(y), end="")
        print()


def vertical_stars_and_stripes():
    for x in range(7):
        for y in range(7):
            if y % 2 == 0:
                print(" -", end="")
            else:
                print(" *", end="")
        print()


def draw_7_border(n):
    for x in range(n):
        print(" *", end="")
    print()
    for x in range(n - 2):
        print(" *", end="")
        for y in range(n - 2):
            print(" -", end="")
        print(" *")
    for x in range(n):
        print(" *", end="")
    print()


def balanced_triangle(n):
    for x in range(2, 2 + n):
        for y in range(1, x):
            print(" " + str(y), end="")
        print()
    for x in range(n, 1, -1):
        for y in range(1, x):
            print(" " + str(y), end="")
        print()


def vertical_triangle(n):
    for x in range(int((n + 1) / 2)):
        print(" " * (int(n / 2) - x), end="")
        print("*" * ((2 - n % 2) + 2 * x))
