"""Prepared with assistance from an AI agent."""


class NumberCollection:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def search(self, value):
        for index, number in enumerate(self.numbers, start=1):
            if number == value:
                return index
        return -1


def main():
    n = int(input("Enter N: "))
    collection = NumberCollection()

    for i in range(n):
        collection.add_number(int(input(f"Enter number {i + 1}: ")))

    x = int(input("Enter X: "))
    print(collection.search(x))


if __name__ == "__main__":
    main()
