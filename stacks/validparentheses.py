# Problem #2: Valid Parentheses
# Given a string s containing characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
# Input: s = "()"
# Output: true

# Input: s = "(]" 
# Output: false

#UMPIRE
#U - Edge Cases:
# Empty string: return False
#if there's only opening or only closing brackets: return false

#M - Have a dictionary with what each match should be and a stack to keep track of the order/sequence of inputs. Then check for the match
#P - 



def validparent( p : str): 

    dictt = {')': '(',  '}': '{',  ']':'['} 
    stackk = [] #new stack
    # bool = True

    for char in p: # ( )

        if char in dictt.values(): 
            stackk.append(char) # stackk == " (, 

        elif  stackk and stackk[-1] == dictt[char] :  #stackk[-1] means stackk at the last position
            stackk.pop()
        else: 
            return False

    return stackk == [] # its supposed to return empty at end. 

print(validparent('(('))