from src.input import GetInput

INPUT = GetInput(1)


def first():
    numbers = INPUT.value.split()
    return sum(int(i) for i in numbers)


def last():
    sum = 0
    frequencies = set()
    while True:
        for i in INPUT.value.split():
            sum += int(i)
            if sum in frequencies:
                return sum
            frequencies.add(sum)


if __name__ == '__main__':
    print('First: ', first())
    print('Last: ', last())
