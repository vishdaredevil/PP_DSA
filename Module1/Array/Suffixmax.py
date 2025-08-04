arr=list(map(int,input().split()))
idx=int(input())
n=len(arr)
smax=[0]*len(arr)
smax[n-1]=arr[n-1]
for i in range(n-2,0,-1):
    smax[i]=max(smax[i+1],arr[i])
    print (smax)
print(smax[idx])
