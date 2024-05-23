list1 = [1, 2, 3, 4, 5, 6]  # Input List 1
list2 = [2, 3, 4, 5, 6, 7]  # Input List 2
list3 = [3, 4, 5, 6, 7, 8]  # Input List 3
set1 = set(list1)  # Convert list1 to set
set2 = set(list2)  # Convert list2 to set
set3 = set(list3)  # Convert list3 to set
Intersection = set1.intersection(set2).intersection(set3)  # Find the common numbers in 3 sets
List = list(Intersection)  # Convert the set to List
print("Duplicates in three lists:", List)  # Print the output
