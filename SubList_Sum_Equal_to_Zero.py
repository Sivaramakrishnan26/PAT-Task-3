list1 = [4,2,-3,1,6]  # Input List
value = 0  # Input value
length = len(list1)  # Length of Input list


def sub_list(list1, value, length):  # Define a function with 3 arguments
    new_list = []
    for i in range(0, length):  # Store the first element as list1[i]
        for j in range(i + 1, length):  # Store the second element as list1[j]
            for k in range(i + 2, length):  # Store the third element as list1[k]
                if list1[i] + list1[j] + list1[k] == value:  # Check the sum of the 3 elements is equal to the given value
                    new_list.append((list1[i], list1[j], list1[k]))
                    # print(f"{list1[i]}, {list1[j]} and {list1[k]}")  # Print the output
    return new_list
    # return False

new_list = sub_list(list1, value, length)  # Call the function
print("Sub List wth sum equal to zero:",new_list)
