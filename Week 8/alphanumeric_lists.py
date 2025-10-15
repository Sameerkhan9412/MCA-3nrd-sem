s = input("Enter a string : ")
l1 = []
l2 = []

for ch in s:
    if((ch.isalpha())):
        l1.append(ch)
    elif(int(ch.isdigit())):
        l2.append(ch)

print(l1)
print(l2)

