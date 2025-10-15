filename = "test"
vowels_count = {}

with open(filename , "r") as file:
    content = file.read()

    for ch in content:
        if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
            if(ch not in vowels_count):
               vowels_count[ch] = 0
            else:
               vowels_count[ch] += 1

print(vowels_count)

max_key = max(vowels_count , key=vowels_count.get)
print(f"Maximum occurrence vowel = ${max_key} with count = {vowels_count[max_key]}")