class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check if it's safe to place a queen at (row, col)
        # Check the same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve(self, row):
        if row == self.n:
            # All queens are placed successfully, add the solution
            self.solutions.append([list(row) for row in self.board])
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve(row + 1)
                self.board[row][col] = 0  # Backtrack

    def nqueens(self):
        self.solve(0)
        return self.solutions

    def print_solution(self, solution):
        for row in solution:
            print(' '.join('Q' if cell == 1 else '.' for cell in row))
        print()

if __name__ == "__main__":
    n = 4  # Change the value of n for different board sizes
    nqueens_solver = NQueens(n)
    solutions = nqueens_solver.nqueens()

    if solutions:
        print(f"Solutions for {n}-Queens:")
        for i, solution in enumerate(solutions, start=1):
            print(f"Solution {i}:")
            nqueens_solver.print_solution(solution)
    else:
        print(f"No solutions found for {n}-Queens.")
