import re

pattern = r'^(1*(01*01*)*)$'

s = input("Enter a string : ")

if(re.fullmatch(pattern , s)):
    print("Matched")
else:
    print("Not matched")