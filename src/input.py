from os import path


class GetInput:
    def __init__(self, day, year='2018'):
        self.year = year
        self.day = day
        self._value = None

    def _filename(self):
        return path.join('inputs', '{} {}.txt'.format(self.year, self.day))

    @property
    def value(self):
        if self._value is None:
            try:
                with open(self._filename()) as f:
                    self._value = f.read()
            except FileNotFoundError:
                return 'File not found'
        return self._value.rstrip("\r\n")
