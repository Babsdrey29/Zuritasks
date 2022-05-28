# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(A1, A2):
    if sorted(A1)== sorted(A2):# [assignment] Add your code here
        print("String is anagram")
    else:
        print("String not anagram")

A1 ="slope"
A2 ="poles"
print("word :", A1)
print("Anagram", A2)
find_anagrams(A1,A2)


