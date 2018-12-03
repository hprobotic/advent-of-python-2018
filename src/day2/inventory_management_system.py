from collections import Counter
from src.input import GetInput

INPUT = GetInput(2)
values = INPUT.value.split()


def first():
    ids_double = 0
    ids_tripple = 0
    for i in values:
        counts = set(Counter(i).values())
        if 2 in counts:
            ids_double += 1
        if 3 in counts:
            ids_tripple += 1

    return ids_double * ids_tripple


def last():
    return 'Last'


if __name__ == '__main__':
    print(first())
    print(last())
