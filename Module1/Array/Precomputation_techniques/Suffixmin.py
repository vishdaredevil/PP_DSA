arr=list(map(int,input().split()))
idx=int(input())
n=len(arr)
smin=[0]*n
smin[n-1]=arr[n-1]
for i in range(n-2,0,-1):
    smin[i]=min(smin[i+1],arr[i])
    print(smin)
print(smin[idx])