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
