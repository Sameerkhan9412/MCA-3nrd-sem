vowels = "aeiouAEIOU"

vowel_counts = {vowel: 0 for vowel in vowels}

# Open and read the file
filename = "input.txt"
with open(filename, 'r') as file:
    content = file.read()

# Count vowels in the file content
for char in content:
    if char in vowel_counts:
        vowel_counts[char] += 1
    combined_counts = {}
    for v in "aeiou":
        lower_count = vowel_counts.get(v, 0)        # count of lowercase vowel
        upper_count = vowel_counts.get(v.upper(), 0)  # count of uppercase vowel
        combined_counts[v] = lower_count + upper_count

max_vowel = max(combined_counts, key=combined_counts.get)
max_count = combined_counts[max_vowel]

print(f"The vowel '{max_vowel}' has the maximum occurrences: {max_count}")
