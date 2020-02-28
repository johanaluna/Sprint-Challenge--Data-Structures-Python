import time

# Importing a binary search Tree:
# because with a binary search we can allocate the element in a dynamic way and also we have 
# methods like contains that help us to compare one elelemnt with other
from binary_search import BinarySearchTree
# Initialize the binary tree with something!
bst = BinarySearchTree("Bucaramanga")

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
 # The first thing to do is add all the element of the list names_1 to the binary searche tree
 # because we nedd a base to compare all the elements of the list name_2
for name in names_1:
    bst.insert(name)

for name2 in names_2:
    if bst.contains(name2):
        duplicates.append(name2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
