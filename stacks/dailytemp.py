        
# helper function that finds what we need and returns count then we exit it , right.
def chkDays(curtemp ): 
    count = 1
    for i in range(1,len(curtemp)): 
        
        if curtemp[i-1] < curtemp[i]: 
            #count += 1
            # print(count)
            return count
            
        else: 
            count += 1
            # print(count)
            #return count
        
    return 0

out = []
temp  = [73,74,75,71,69,72,76,73]

N = len(temp)
    
for i in range( N ): 
        
    out.append(chkDays(temp[i:]))
            
print(out)
            