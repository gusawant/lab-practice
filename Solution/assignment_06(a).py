# Create a list of integers from 1 to 10
my_list = list(range(1, 11))

# i. Add the number 15 at the end of the list
my_list.append(15)
print("After adding 15 at the end:", my_list)

# ii. Insert the number 5 at the 2nd index
my_list.insert(2, 5)
print("After inserting 5 at the 2nd index:", my_list)

# iii. Remove the number 8 from the list
my_list.remove(8)
print("After removing 8 from the list:", my_list)

# iv. Sort the list in descending order
my_list.sort(reverse=True)
print("After sorting in descending order:", my_list)

# v. Find the length of the list
length_of_list = len(my_list)
print("Length of the list:", length_of_list)

# vi. Retrieve the first and last elements of the list
first_element = my_list[0]
last_element = my_list[-1]
print("First element:", first_element)
print("Last element:", last_element)
