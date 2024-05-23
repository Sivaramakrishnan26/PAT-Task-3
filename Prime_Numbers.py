list1 = [10, 501, 22, 37, 100, 999, 87, 351]  # Input List
print("Input List =", list1)  # Print the input list


# Prime_Numbers = list(filter(lambda x: all(x % y != 0 for y in range(2, int(x**0.5) + 1)), list1))
# print("Prime Numbers =", Prime_Numbers)

def prime_num(x):  # Define a function
    if x < 2:  # Check x less than 2
        return False  # Return False, Since less than 2 are not prime
    for i in range(2, int(x ** 0.5) + 1):  # Iterates from 2 to sqrt of x
        if x % i == 0:  # Check x is divisible by i
            return False  # Return False, since x is not a prime number
    return True  # Return True, If no divisors are found


Prime_Numbers = [x for x in list1 if prime_num(x)]  # For each x in list1, check whether it is prime using prime_num(x)
print("Prime Numbers =", Prime_Numbers)  # Print the output
