'''
Given an array of strings queries and a string pattern, return a boolean array answer
 where answer[i] is true if queries[i] matches pattern, and false otherwise.

A query word queries[i] matches pattern if you can insert lowercase English letters pattern so that it equals the query. 
You may insert each character at any position and you may not insert any characters.

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false] 

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
 
'''
# UMPIRE
# U: Edge case: 
    # String is empty
    # Only has one of the chars from the pattern
# P; 
#Option 01
# Loop, check isupper()? , if not in pattern, return false

# Option 02:
# Loop, check isupper()? put all uppercase letters in another string then compare with the pattern

# Match: Append the true,false results into an output array
# Option 01: loop, isupper()
# Option 02: loop, isupper(), string to store result

# query[i] = FooBar pattern = FB

# Two Pointers:
def queryPattern(queries :list, pattern : str):
    output = [] # array of booleans
    p1 = p2 = 0 

    for query in queries: 

        if query[p1].isupper():

            if query[p1] != query[p2]: 
                output.append(False)
                p2 += 1
                break 
        
        if p2 < len(pattern):
            p2 += 1
        
        if p1 == len(query[p1]) -1: 
            output.append(True)
            continue
        
        print(query)
        
        p1 += 1
       
        

    return output

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"

# Regex - Allows you to search a string for a match ;- search() function in regex



