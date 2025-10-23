import re

def has_even_zeros(s):
    # Check if string contains only 0 and 1
    if not re.fullmatch(r'[01]*', s):
        return False

    # Count zeros
    zero_count = s.count('0')

    # Check if zero_count is even
    return zero_count % 2 == 0

# Test examples
test_strings = ['1010', '11011', '000', '111', '1001']

for ts in test_strings:
    if has_even_zeros(ts):
        print(f"'{ts}' has an even number of 0s.")
    else:
        print(f"'{ts}' does NOT have an even number of 0s.")
