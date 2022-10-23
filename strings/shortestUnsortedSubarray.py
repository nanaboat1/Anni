'''
Given an array, find the length of the smallest subarray in it which 
when sorted will sort the whole array.

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

''' 
# u - if null or len(input) == 1: return 0 
# m - two pointers approach. 
# p - itr over array , and when you meet a sequence that specifies the criteria, then you check it out. 

from threading import local


def unSort( nums : list) : 

    # edge-case
    if len(nums) <= 1 : return 0 

    
    N = len(nums) 
    left, right = 0, N - 1 

    

    while left < right and nums[left] <= nums[left + 1]:
        left += 1           
       
    
    if left == right: 
        return 0 

    while right > 0 and nums[right] >= nums[right-1]: 
        right -= 1 
    
    localmin = min(nums[left:right+1]) 
    # print(nums[left:right+1])

    while left > 0 and nums[left-1] > localmin: 
        left -= 1 

    localmax = max(nums[left:right+1])

    while right < N-1 and nums[right+1] < localmax: 
        right += 1


    # if localmin < nums[left]: 
    #print(right - left +1)
    return right - left + 1 
        

def main():
  tests = [
    { 'input': [], 'output': 0 },
    { 'input': [5], 'output': 0 },
    { 'input': [1,2,3], 'output': 0 },
    { 'input': [3,2,1], 'output': 3 },
    { 'input': [1,2,3,2], 'output': 2 }, # 3,2
    { 'input': [1,2,5,3,7,10,9,12], 'output': 5 }, # 5,3,7,10,9
    { 'input': [1,3,2,0,-1,7,10], 'output': 5 }, # 1,3,2,0,-1   #1 3 2 0 -1
    { 'input': [1,2,3,11,8,9,10], 'output': 4 }, # 11,8,9,10
  ]

  for i in range(len(tests)):
    print(f'Test {i+1}:', unSort(tests[i]['input']) == tests[i]['output'])

main()