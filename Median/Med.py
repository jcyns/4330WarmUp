# Function to calculate the median of a list of integers
def calculateMedian(numbers):
    numbers.sort() 
    n = len(numbers)
    middle = n // 2

    # If odd number of elements, return the middle one
    if n % 2 == 1:
        return numbers[middle]
    # If even number of elements, return the average of the middle two
    else:
        return (numbers[middle - 1] + numbers[middle]) / 2

userInput = input("Enter integers separated by spaces: ")

# Convert the input string to a list of integers
numbers = list(map(int, userInput.split()))

# Calculate and display the median
if numbers:
    median = calculateMedian(numbers)
    print(f"The median is: {median}")
else:
    print("No integers entered.")
