import stacks.linkedlist as ll


# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false



# if s[i] not in dictt.keys():
#     #add it to dictt
# else:
#     #check if the value of s[i] key corresponds to t[i]
# # dictt = {e:a, g:d, } ---> keys:s[i], value:t[i]


##  s = egg , t = add 
##  S = { e: a, g:d, g:d}, T = { a:e, d:g, d:g}

##




# egg == adt, 

def isIsomorphic( s : str, t : str) -> bool :
    #Option 01
    #Edge Case
    # if len(s) == 1:
    #     return True
    # #store the maps from s[i] to t[i] on a dict
    # dictt = {}
    # booll = True #keep track
    # for i in range(len(s)):
    #     if s[i] not in dictt.keys():
    #         dictt[s[i]] = t[i] 
    #     elif t[i] in dictt.values():
    #         return False
    #     else:
    #         booll =  dictt[s[i]] == t[i]
    #         if booll == False:
    #             return False
            

    # return booll 

    #Option 02
    if len(s) == 1:
        return True
    
    S = {} #dict for s
    T = {} #dict for t

    for i in range(len(s)):
        S[s[i]] = t[i]
        T[t[i]] = s[i]
    
    return list(S.keys()) == list(T.values())




print(isIsomorphic('badc', 'baba'))