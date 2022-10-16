from collections import Counter

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 
using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""
#UMPIRE
#Edge Cases:
# the string have len of 1
# strings may have different lengths

#Match 
# -> Dictionaries to store the characters and their frequncies

#Plan
# Option 01:
# Loop through each string and save the characters into a dictionary
#-> if the dictionaries are similar, then t is an anagram of s
#Option 02:
#Putting the characters into a set/array, if they are similar then strings are the same

#Implement:

def isAnagram( s:str, t:str) -> bool:

    S, T = Counter(s), Counter(t)
    # S = {} #dict for s
    # T = {} #dict for t

    return S == T

print(isAnagram("add",  "dad"))