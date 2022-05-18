def display_array(rows, columns):
    a = []

    for i in range(0, rows):
        b = []

        for j in range(0, columns):
            print("Enter the {0} {1} th element".format(i, j))
            c = int(input())
            b.append(c)
        a.append(b)

    return a


if __name__ == "__main__":
    row = int(input("Enter no.of rows "))
    column = int(input("Enter no.of columns "))
    array_element = display_array(row, column)
    print(array_element)
