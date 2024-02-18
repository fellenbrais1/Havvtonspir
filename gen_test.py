# This test doesn't work for now, there is still more I need to learn here

class NumberGen:
    def __init__(self, start=0):
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > 10:
            raise StopIteration
        value = self.value
        self.value += 1
        return value


def number_gen():
    return NumberGen()
