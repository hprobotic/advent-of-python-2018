from src.input import GetInput

INPUT = GetInput(1)


def first():
    numbers = INPUT.value.split()
    return sum(int(i) for i in numbers)


def last():
    return str('Last')


if __name__ == '__main__':
    print('First: ', first())
    print('Last: ', last())
