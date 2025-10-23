input_str = input("Enter a string with letters and numbers: ")

L1 = []  # to store numbers
L2 = []  # to store alphabets

for char in input_str:
    if char.isdigit():
        L1.append(char)
    elif char.isalpha():
        L2.append(char)

# Print the results
print("List of numbers (L1):", L1)
print("List of alphabets (L2):", L2)
