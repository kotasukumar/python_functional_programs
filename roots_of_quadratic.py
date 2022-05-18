import math


def calculate_root(a, b, c):
    delta = b * b - 4 * a * c
    first_root = (-b + math.sqrt(delta)) / 2 * a
    second_root = (-b - math.sqrt(delta)) / 2 * a

    return first_root, second_root


if __name__ == "__main__":
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    first_root, second_root = calculate_root(a, b, c)
    print(first_root, second_root)
