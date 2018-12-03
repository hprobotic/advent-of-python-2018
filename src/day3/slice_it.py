from src.input import GetInput

INPUT = GetInput(3)


def first():
    return str('First')


def last():
    return str('Last')


if __name__ == '__main__':
    print(first())
    print(last())
