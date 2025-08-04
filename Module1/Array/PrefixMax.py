arr=list(map(int,input().split()))
pmax=[0]*len(arr)
idx=int(input())
n=len(arr)
pmax[0]=arr[0]
for i in range(1,n):
    pmax[i]=max(pmax[i-1],arr[i])
    # print(pmax)
print(pmax[idx])