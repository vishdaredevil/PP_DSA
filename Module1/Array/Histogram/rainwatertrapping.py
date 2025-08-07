#This is also a leetcode question
#https://leetcode.com/problems/trapping-rain-water/
#my solution :
def trap(height):
    n=len(height)
    left=[0]*n
    left[0]=height[0]
    for i in range(1,n):
        left[i]=max(left[i-1],height[i])
    right=[0]*n
    right[-1]=height[-1]
    for i in range(n-2,0,-1):
        right[i]=max(right[i+1],height[i])
    amount=0
    for i in range(1,n-1):
        deciding_ht=min(left[i],right[i])
        if (deciding_ht>height[i]):
            amount+=deciding_ht-height[i]
    return amount
height=list(map(int,input().split()))    
print(trap(height))       
