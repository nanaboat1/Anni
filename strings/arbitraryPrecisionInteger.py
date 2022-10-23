'''
Bonus Problem: Increment an arbitrary precision integer
Implement a function to increment an arbitrary precision integer represented in the form of an array, where each element in the array corresponds to a digit.

Examples:
Input: [1,2,3]
Output: [1,2,4]
Explanation: 123 + 1 = 124

Input: [5,8,9]
Output: [5,9,0]
Explanation: 589 + 1 = 590
'''

# UMPIRE
def arbitrary(arr : list):
    # arr[-1] += 1 happy cases [1,3,6,7,4,6,8] 

    arr = [ str(i) for i in arr] 

    word = "".join(arr) 

    num = int(word) + 1 

    wordd = str(num) 

    arr_out = list(wordd) 

    arr_out = [ int(i) for i in arr_out]
 
    return arr_out 


print(arbitrary([9,9,9,9,9]))
        
