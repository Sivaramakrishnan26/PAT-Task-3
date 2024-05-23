list1 = [10, 501, 22, 37, 100, 999, 87, 351]  # Input List
print("Input List =", list1)  # Print the input list


def happy_num(x):  # Define a function
    Happy_Numbers = []  # Create a empty list to store the happy numbers
    while x != 1 and x not in Happy_Numbers:  # Continue the loop until x not equal to 1 and x not already in Happy_Numbers
        Happy_Numbers.append(x)  # Append the Happy Numbers to the Happy_Numbers list
        x = sum(int(digit) ** 2 for digit in str(x))
    return x == 1  # If x equals 1, then it's a happy number


Happy_Numbers = [x for x in list1 if happy_num(x)]  # For each x in list1, check whether it's a happy number using happy_num(x)
print("Happy Numbers =", Happy_Numbers)  # Print the Output
