list1 = [10, 501, 22, 37, 100, 8, 999, 87, 351]  # Input List
print("Input List =", list1)  # Print the input list


# a = sorted(list1)  # Sort the list
# print("Minimum element is", a[0])  # Print the 1st element in a sorted list

def min_element(list1):  # Define a function
    x_min = list1[0]  # Initialize a variable x_min with value as first element of list1
    for i in range(len(list1)):  # Iterates through all the elements in the list1
        if list1[i] < x_min:  # Compare the current element with x_min
            x_min = list1[i]  # If the current element is less than x_min, replace the current element as x_min
    return x_min


print("Minimum element is", min_element(list1))  # Print the output
