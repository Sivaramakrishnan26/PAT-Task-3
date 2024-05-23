list1 = [10, 20, 30, 9]  # Input List
value = 59  # Input value
length = len(list1)  # Length of Input list


def triplet(list1, value, length):  # Define a function with 3 arguments
    for i in range(0, length - 2):  # Store the first element as list1[i]
        for j in range(i + 1, length - 1):  # Store the second element as list1[j]
            for k in range(j + 1, length):  # Store the third element as list1[k]
                if list1[i] + list1[j] + list1[k] == value:  # Check the sum of the 3 elements is equal to the given value
                    print(f"Triplet is {list1[i]}, {list1[j]} and {list1[k]}")  # Print the output
                    return True
    return False


triplet(list1, value, length)  # Call the function
