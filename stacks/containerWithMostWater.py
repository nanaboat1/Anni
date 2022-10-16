# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
#  of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

 
def maxArea(height: list) -> int:
    i = 0
    j = len(height) - 1
    area = 0 #maximum amount of water a container can store.
    maxx = 0
    while i < j:
        area = (j-i) * min(height[j], height[i])
        if maxx < area:
            maxx = area
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1    

    return maxx
height = [1,8,6,2,5,4,8,3,7]
h2 = [1,1]
print(maxArea(h2))