# Open and read files
with open('file1.txt', 'r') as f1:
    file1_lines = f1.readlines()

with open('file2.txt', 'r') as f2:
    file2_lines = f2.readlines()

# Find middle line index of file1
middle_index_file1 = len(file1_lines) // 2  # integer division

# Find last line index of file2
last_index_file2 = len(file2_lines) - 1

# Swap lines
file1_lines[middle_index_file1], file2_lines[last_index_file2] = file2_lines[last_index_file2], file1_lines[middle_index_file1]

# Write back to files
with open('file1.txt', 'w') as f1:
    f1.writelines(file1_lines)

with open('file2.txt', 'w') as f2:
    f2.writelines(file2_lines)

print("Swap done successfully!")
