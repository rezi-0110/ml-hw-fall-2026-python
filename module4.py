def find_index(numbers, x):
    if x in numbers:
        return numbers.index(x) + 1
    return -1


def main():
    n = int(input("Enter N: "))

    numbers = []
    for i in range(n):
        numbers.append(int(input(f"Enter number {i + 1}: ")))

    x = int(input("Enter X: "))
    print(find_index(numbers, x))


if __name__ == "__main__":
    main()
