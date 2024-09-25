# Function to calculate the average of a list of numbers
def calculateAvg(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Get user input
userInput = input("Enter numbers separated by spaces: ")

# Convert the input string to a list of numbers
numbers = list(map(float, userInput.split()))

# Calculate and display the average
if numbers:
    avg = calculateAvg(numbers)
    print(f"The average is: {avg}")
else:
    print("No numbers entered.")
