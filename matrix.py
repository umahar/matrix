class Matrix:
    def __init__(self, matrix_string):
        self.matrix = self.create_matrix(matrix_string)

    def create_matrix(self, m_string):
        # Split the string by newlines for rows and by spaces for elements
        return [list(map(int, row.split())) for row in m_string.splitlines()]

    def row(self, index):
        # Return the row at the 1-based index
        return self.matrix[index - 1]

    def column(self, index):
        # Return the column at the 1-based index
        return [row[index - 1] for row in self.matrix]


# Example usage
matrix = Matrix("9 8 7\n5 3 2\n6 6 7")
print(matrix.row(2))  # [5, 3, 2]
print(matrix.column(2))  # [8, 3, 6]
