class Solution:
    # Function to print the number pattern
    def pattern3(self, N):
        # Outer loop for rows
        for i in range(1, N + 1):
            # Inner loop for columns
            # Print numbers from 1 to i
            for j in range(1, i + 1):
                print(j, end=" ")
            # Move to the next row
            print()

if __name__ == "__main__":
    # Create object of Solution class
    sol = Solution()

    # Define size of pattern
    N = 5

    # Call pattern function
    sol.pattern3(N)
