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
            # If all queens are placed, add the solution
            self.solutions.append(self.columns[:])
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                # If it's safe to place a queen in the current row and column
                self.columns[row] = col  # Place the queen
                self.solve(row + 1)  # Recursively solve for the next row

                # Backtrack: If the recursive call didn't find a solution, remove the queen
                self.columns[row] = -1

def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in range(len(solution)):
            line = ["Q" if solution[row] == col else "." for col in range(len(solution))]
            print(" ".join(line))
        print("\n")

def main():
    n = 4  # Change this to the desired board size
    csp = NQueensCSP(n)
    csp.solve()

    if csp.solutions:
        print(f"Found {len(csp.solutions)} solution(s) for {n}-Queens:")
        print_solutions(csp.solutions)
    else:
        print(f"No solution found for {n}-Queens.")

if __name__ == "__main__":
    main()
