import time
from doubly_linked_list import DoublyLinkedList

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# starting solution: runtime O(n^2)
    # takes ~ 6.7 seconds

# duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
    # for name_2 in names_2:
        # if name_1 == name_2:
            # duplicates.append(name_1)

# solution using dll:

# duplicates = []

# stretch solution using sets:
    # takes ~ 0.007 seconds

# set_1 = set(names_1)
# set_2 = set(names_2)

# duplicates = set_1.intersection(set_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
