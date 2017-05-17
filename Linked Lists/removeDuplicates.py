# Write code to remove duplicates from an unsorted linked list
# Assume the input is integer, sort the linked list first, if the input is 
# of string, sort the linked list based on the converted string to integer
# Loop through the input and compare. Only need one buffer.
# Even better, just use a hash table to compare and delete as we traverse the linked list
# It only takes O(n)


def removeDuplicates(linkedList):
	D = {};
	newList = [];
	for element in linkedList:
		if not element in D.keys():
			D[element] = 1
			newList.append(element)
	return newList

if __name__ == "__main__":
	linkedList = [5,6,5,5,4,3,2,4,6,6,4,3,7,8,9,3,3,5,6,3,2,1,5,7,9,6,5,4,2,11,12,13,14,3,3,5,6,7]
	newList = removeDuplicates(linkedList)
	print (newList)

# This solution runs in O(n) time if instead of checking if element is in list of keys we check
# by just inserting it and see if it duplicates