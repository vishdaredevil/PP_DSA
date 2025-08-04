#PREFIX SUM BY PRECOMPUTATION TECHNIQUE
# This code computes the prefix sum of an array and allows for efficient range sum queries.
arr=list(map(int, input().split()))
l=int(input())
r=int(input())
n=len(arr)
ps = [0]*n
ps[0]=arr[0]
for i in range(1,n):
    ps[i]=ps[i-1]+arr[i]
if l==0:
    print(ps[r])
else:
    print(ps[r]-ps[l-1])
