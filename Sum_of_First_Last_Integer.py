x = int(input("Enter an Integer: "))  # Get an input integer from the user
y = str(x)  # Convert the integer into string
a = int(y[0])  # Convert the first string into an integer
b = int(y[-1])  # Convert the last string into an integer
c = a + b  # Add the first and last number
print(f"The sum of {a} and {b} is", c)  # Print the output
