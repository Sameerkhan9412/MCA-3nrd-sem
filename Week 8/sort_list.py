elements = input("Enter even no of elements : ").split()
elements.sort()

mid = len(elements) // 2

l1 = elements[:mid]
l2 = elements[mid:len(elements)]   

print(l1)
print(l2)