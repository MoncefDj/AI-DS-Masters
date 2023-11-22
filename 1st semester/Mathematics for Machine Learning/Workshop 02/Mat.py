import numpy as np


class Mat:
    matMulCheck = lambda A, B: A.shape[1] == B.shape[0]
    matMul = lambda A, B: np.array(
        [
            [sum(a * b for a, b in zip(row, col)) for col in B.T]
            for row in A
            if Mat.matMulCheck(A, B)
        ]
    )

    @staticmethod
    def augmentedMat(A, b):
        rows, cols = A.shape

        augmented1 = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(A[i, j])
            row.append(b[i])
            augmented1.append(row)

        augmented2 = []
        for i in range(rows):
            row = np.concatenate((A[i], [b[i]]))
            augmented2.append(row)

        return np.array(augmented1), np.array(augmented2)

    @staticmethod
    def gaussianElimination(A):
        n = len(A)

        for i in range(n):
            pivot_row = i
            for j in range(i + 1, n):
                if abs(A[j, i]) > abs(A[pivot_row, i]):
                    pivot_row = j

            A[[i, pivot_row]] = A[[pivot_row, i]]

            for j in range(i + 1, n):
                factor = A[j, i] / A[i, i]
                A[j] -= factor * A[i]

        return A

    @staticmethod
    def solveLinearSystem(A, b):
        A = np.asarray(A, dtype=np.float64)
        b = np.asarray(b, dtype=np.float64)
        n = len(A)
        Ab = Mat.augmentedMat(A, b)[0]
        Ab = Mat.gaussianElimination(Ab)

        solution = np.zeros(n)
        for i in range(n - 1, -1, -1):
            solution[i] = (Ab[i, -1] - np.dot(Ab[i, :-1], solution)) / Ab[i, i]

        return solution

    @staticmethod
    def isSubspace(S):
        if len(S) == 0:
            return True

        dimension = len(S[0])
        for vector in S:
            if len(vector) != dimension:
                return False

        augmented_matrix = Mat.augmentedMat(S, np.zeros(S.shape[0]))[0]
        row_echelon_form = Mat.gaussianElimination(augmented_matrix)

        for row in row_echelon_form:
            if np.count_nonzero(row[:-1]) == 0 and row[-1] != 0:
                return False

        rank = np.count_nonzero(row_echelon_form[:, :-1], axis=1)
        if rank.size == dimension:
            return True
        else:
            return False

    @staticmethod
    def det(A):
        if A.shape[0] != A.shape[1]:
            raise ValueError("Matrix must be square to calculate the determinant.")

        if A.shape[0] == 2:
            return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
        else:
            det_value = 0
            for j in range(A.shape[1]):
                submatrix = np.delete(A, 0, axis=0)
                submatrix = np.delete(submatrix, j, axis=1)
                det_value += (
                    (-1) ** (j) * A[0, j] * Mat.det(submatrix)
                )

            return det_value
