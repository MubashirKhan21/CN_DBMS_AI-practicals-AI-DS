class NQueensCSP:
    def __init__(self, n):
        self.n = n
        self.columns = [-1] * n  # List to represent column assignments for queens
        self.solutions = []

    def is_safe(self, row, col):
        for prev_row in range(row):
            if self.columns[prev_row] == col or \
               self.columns[prev_row] - prev_row == col - row or \
               self.columns[prev_row] + prev_row == col + row:
                return False
        return True

    def solve(self, row=0):
        if row == self.n:
            self.solutions.append(self.columns[:])
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.columns[row] = col
                self.solve(row + 1)
                self.columns[row] = -1

def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in range(len(solution)):
            line = ["Q" if solution[row] == col else "." for col in range(len(solution))]
            print(" ".join(line))
        print("\n")

def n_queens_solver(n):
    csp = NQueensCSP(n)
    csp.solve()
    return csp.solutions

if __name__ == "__main__":
    n = 8  # Change this to the desired board size
    solutions = n_queens_solver(n)
    if solutions:
        print(f"Found {len(solutions)} solution(s) for {n}-Queens:")
        print_solutions(solutions)
    else:
        print(f"No solution found for {n}-Queens.")
