# mangoes = [10, 501, 22, 37, 100, 8, 999, 87, 351]
mangoes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(sorted(mangoes))
students = int(input("Enter the number of Students: "))


def distribute_mangoes(mangoes, students):
    mangoes.sort()  # Sort the mangoes in ascending order
    n = len(mangoes)
    min_diff = float('inf')  # Initialize minimum difference

    # Calculate the minimum difference
    for i in range(n - students + 1):
        diff = mangoes[i + students - 1] - mangoes[i]
        # print(f"{mangoes[i + students - 1]} - {mangoes[i]}", diff)
        min_diff = min(min_diff, diff)

    # Allocate bags to students
    allocation = [[] for x in range(students)]
    for i in range(n):
        allocation[i % students].append(mangoes[i])

    return allocation, min_diff


result, min_difference = distribute_mangoes(mangoes, students)

print("Minimum Difference:", min_difference)  # Print the Minimum Difference
for i, bags in enumerate(result):
    print(f"Student {i + 1} gets bags:", bags)  # Print the output
