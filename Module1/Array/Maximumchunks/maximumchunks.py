# https://leetcode.com/problems/max-chunks-to-make-sorted/description/
#in this i used the concept of prefux max and also i used the concept of greedy.
from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
    #     n=len(arr)
    #     i=0
    #     ans=0
    #     while i<n:
    #         for j in range(i,n):
    #             if (self.canbechuked(arr,i,j)):
    #                 ans=ans+1
    #                 i=j+1
    #                 break   
    #     return ans
    # def canbechuked(self, arr: list[int], i: int, j: int) -> bool:
    #     count=0
    #     for k in range(i,j+1):
    #         if arr[k]>=i and arr[k]<=j:
    #             count=count+1
    #     if count==(j-i+1):
    #         return True
    #     else:
    #         return False
        n=len(arr)
        if len(arr)<=1:
            return 1
        ans=0
        pmax=[0]*len(arr)
        pmax[0]=arr[0]
        for i in range(1,n):
            pmax[i]=max(pmax[i-1],arr[i])
        for i in range(n):
            if pmax[i]==i:
                ans=ans+1
        
        return ans