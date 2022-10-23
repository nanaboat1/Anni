'''
Given an input string, write a function that returns the run-length encoded string for the input string.*

Example:
Input: "wwwwaaadexxxxxx"
Output: "w4a3d1e1x6"
'''
# UMPIRE:
# U :
# Edge cases:
# string is empty, return None
# string has len 1, return string1
# each of the letters only appears once
# M:
# two pointers; next to each other, int count to store the freq, output string to return the encoded input
# P: 
# itr through the string and check if the pointers point to the same thing, if so, make first pointer
def encoding(word: str): #aaa
    s = ''
    if len(word) == 0:
        return None
    if len(word) == 1:
        s = word + '1'
    p1, p2 = 0, 1 #a  a  a
                #     p1 p2
    freq = 1
    while p2 < len(word): # a a a 
        if word[p2] == word[p1]:
            freq += 1 #freq = 3
             #p2 = 2
        
        if p2 == len(word) - 1:
            s = s + word[p1] + str(p2 - p1 + 1)
        
        if word[p2] != word[p1]:
            s = s + word[p1] + str(p2 - p1 )
            p1 = p2
        p2 += 1 
        

    print(s) 
    return s

#



def main():
  tests = [
    { 'input': "", 'output': None },
    { 'input': "w", 'output': "w1" },
    { 'input': "aaa", 'output': "a3" },
    { 'input': "wwwwaaa", 'output': "w4a3" },
    { 'input': "wwwwaaadexxxxxx", 'output': 'w4a3d1e1x6' }, # 3,2
    #{ 'input': [1,2,5,3,7,10,9,12], 'output': 5 }, # 5,3,7,10,9
    #{ 'input': [1,3,2,0,-1,7,10], 'output': 5 }, # 1,3,2,0,-1   #1 3 2 0 -1
    #{ 'input': [1,2,3,11,8,9,10], 'output': 4 }, # 11,8,9,10
  ]

  for i in range(len(tests)):
    print(f'Test {i+1}:', encoding(tests[i]['input']) == tests[i]['output'])

main()