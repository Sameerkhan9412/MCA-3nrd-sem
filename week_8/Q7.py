while True:
    user_input = input("Enter distinct integers separated by spaces (even number of elements): ")
    nums = user_input.split()

    # Convert to integers
    try:
        nums = list(map(int, nums))
    except ValueError:
        print("Please enter valid integers.")
        continue

    # Check distinctness
    if len(nums) != len(set(nums)):
        print("Numbers are not distinct. Try again.")
        continue

    # Check even length
    if len(nums) % 2 != 0:
        print("Number of elements is not even. Try again.")
        continue

    break

nums.sort()

# Split into two lists
mid = len(nums) // 2
L1 = nums[:mid]
L2 = nums[mid:] 

for i in range(mid):
    if L1[i] >= L2[i]:
        print("Cannot ensure L1 elements are less than L2 elements for all positions.")
        break

print("First list (L1):", L1)
print("Second list (L2):", L2)
