

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join([str(i) for i in m]) for m in self.matrix])

    def __add__(self, other):
        try:
            numb = [[int(self.matrix[i][m]) + int(other.matrix[i][m]) for i in range(len(self.matrix[m]))]
                for m in range(len(self.matrix))]
            return Matrix(numb)
        except IndexError:
            print('Matrix size Error')

width = int(input('Input amount of lines and columns in matrix: '))
height = width

m1 = Matrix([[i*m for m in range(width)] for i in range(height)])
m2 = Matrix([[i*m for m in range(width)] for i in range(height)])

print('The first:\n', m1)
print('The second:\n', m2)
print('Sum:\n', m1 + m2)






