class Matrix:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for i in range(len(self.list_1)):
            for x in range (len(self.list_2)):
                matrix[i][x] = self.list_1[i][x] + self.list_2[i][x]

        return str('\n'.join(['\t'.join([str(x) for x in i]) for i in matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(x) for x in i]) for i in matrix]))


test_matrix = Matrix([
            [2, 3, 5],
            [2, 5, 2],
            [6, 1, 1],
        ],[
            [5, 7, 8],
            [2, 3, 9],
            [1, 1, 1],
        ]
)
print(test_matrix.__add__())
