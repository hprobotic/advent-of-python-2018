from src.input import GetInput

INPUT = GetInput(1)


def first():
    numbers = INPUT.value.split()
    return sum(int(i) for i in numbers)


def last():
    total = 0
    frequencies = set()
    while True:
        for i in INPUT.value.split():
            total += int(i)
            if total in frequencies:
                return total
            frequencies.add(total)


if __name__ == '__main__':
    print('First: ', first())
    print('Last: ', last())
