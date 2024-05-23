list1 = [10, 501, 22, 37, 100, 999, 87, 351]  # Input List
print("Input List =", list1)  # Print the input list


def even_odd(list1):  # Define a function
    even_list = []  # Empty list to store even numbers
    odd_list = []  # Empty list to store odd numbers
    for i in list1:  # Iterates each element i in input list
        if i % 2 == 0:  # TO check the element is even. Remainder is 0 when divided by 2
            even_list.append(i) # If the element is even, Append it to the new list 'even_list'
        else:
            odd_list.append(i) # If the element is odd, Append it to the new list 'odd_list'
    return even_list, odd_list  # Return both even and odd list


even_list, odd_list = even_odd(list1)  # Call the function
print("Even List =", even_list)  # Print even list
print("Odd List =", odd_list)  # Print odd list

# Using lambda
# even_list = list(filter(lambda x : x % 2 == 0, list1))
# odd_list = list(filter(lambda x : x % 2 != 0, list1))
# print("Even List =",even_list)
# print("Odd List =",odd_list)
