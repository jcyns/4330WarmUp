# Function to calculate the sum of a list of integers
def calculateSum(numbers):
    return sum(numbers)

# Get user input
userInput = input("Enter integers separated by spaces: ")

# Convert the input string to a list of integers
numbers = list(map(int, userInput.split()))

# Calculate and display the sum
if numbers:
    totalSum = calculateSum(numbers)
    print(f"The sum is: {totalSum}")
else:
    print("No integers entered.")
