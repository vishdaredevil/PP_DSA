arr=list(map(int,input().split()))
pmin=[0]*len(arr)
idx=int(input())
n=len(arr)
pmin[0]=arr[0]
for i in range(1,n):
    pmin[i]=min(pmin[i-1],arr[i])
    print(pmin)
print(pmin[idx])