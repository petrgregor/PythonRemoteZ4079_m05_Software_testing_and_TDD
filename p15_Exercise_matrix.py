class Matrix:
    _data = []

    def __init__(self, data_):
        self.data = data_

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data_):
        # check dimensions
        for r in data_:
            if len(r) != len(data_[0]):
                raise ValueError
        self._data = data_

    def __repr__(self):
        return f"Matrix({self._data})"

    def __str__(self):
        result = ""
        for r in self._data:
            for c in r:
                result += f"{c}\t"
            result += "\n"
        return result

    def transpose(self):
        transposed = []
        for i in range(len(self.data[0])):
            new_row = [self.data[j][i] for j in range(len(self.data))]
            transposed.append(new_row)
        return Matrix(transposed)


if __name__ == "__main__":
    m = Matrix([[1, 2], [3, 4]])
    print(m)
    mt = m.transpose()
    print(mt)
    m2 = Matrix([[1, 2, 3], [4, 5, 6]])
    mt2 = m2.transpose()
    print(m2)
    print(mt2)

    try:
        m3 = Matrix([[1, 2, 3], [1, 2]])
    except ValueError as e:
        print(repr(e))
