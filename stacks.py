# nana and anni 

# Problem #1: Evaluate Postfix expression
# Write a function to evaluate the value of an expression in postfix notation represented by a string with 
# numbers between 0 and 9 and operators separated by whitespace. The expression supports 4 
# binary operators '+', '*', '-' and '/'.

# Example:
# Input: "5 1 2 + 4 * + 3 -"
# Output: 14
# The expression is evaluated as follows:
# 5 3 4 * + 3 - DEF
# 5 12 + 3 -
# 17 3 -
# 14

def postfix(expr : str):
    ops = { '+': lambda x,y: x + y, '-':lambda x,y : x - y,'*': lambda x,y:x * y, '/' : lambda x,y: x / y} 
    # UMPIRE
    # u - lets assume there will be equivalent numbers and operations to work with.
    # m - use two stacks, one for operation and one for numbers. 
    # p - iterate over the string, and if we meet a number add to number stack, and if we meet an ops add to operation stack. 

    num = []
    # apr 1 : itr over input and add to respective stacks. 

    for char in expr: 

        if char not in ops and char != ' ':     
            num.append(int(char)) 
        
        if char in ops: 
            numA = int(num.pop())
            numB = int(num.pop())
            
            num.append(ops[char](numB, numA)) 
    

    return num.pop()


# test the fxn. 
print(postfix('5 3 4 * + 3 -')) 

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
#U - Edge Cases: Empty string: return False
#M - Have a dictionary with what each match should be and a stack to keep track of the order/sequence of inputs. Then check for the match
#P - 

