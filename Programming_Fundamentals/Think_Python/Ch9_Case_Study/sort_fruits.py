# open up unsorted_fruits.txt file in read mode
infruits = open("unsorted_fruits.txt", 'r')

# open a sorted_fruits.txt file in write mode
outfruits = open("sorted_fruits.txt", 'w')

# create a list to hold the contents of our infruits file
container = infruits.readlines()

# roll through the list and remove the spaces between each item
for item in container:
    if item == '\n':
        container.remove(item)

# sort the remaining contents of the container list
container.sort()

# roll through the list and add each item to our outfruits file
# also add a space after each item, so it mirrors infruit file
for item in container:
    outfruits.write(item)
    outfruits.write('\n')

# close our outfruits and infruits files
outfruits.close()
infruits.close()