list1 = [684, 28, 84, 33, 86, 28, 86, 654, 23, 33]  # Input List

Repeat_List = []  # Empty list to store Repeating elements
Non_Repeat_List = []  # Empty list to store Non-Repeating elements

for x in list1:  # Iterates through each x in list1
    if x in Repeat_List:  # Check if the current element is in Repeat_list
        continue  # Then skip to the next element
    if x in Non_Repeat_List: # Check if the current element is in Non_Repeat_list. If present, it means the element is repeating
        Non_Repeat_List.remove(x)  # Remove the element from the Non_Repeat_List
        Repeat_List.append(x)  # Add that element to the Repeat_List
    else:
        Non_Repeat_List.append(x)  # If the current element is not in either list, add it to the Non_Repeat_List
print("Non-Repeated Elements in a List:", Non_Repeat_List)  # Print the output
