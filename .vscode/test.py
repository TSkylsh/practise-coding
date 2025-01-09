n,w = map(int,input().split())
inputs = [[0]*(n+1)for _ in range(2)]
weights = inputs[0]
values = inputs[1]
dp=[0]*(w+1)
for i in range(1,n+1):
    inputs[0][i],inputs[1][i]=map(int,input().split())
for i in range(1,n+1):
    for j in range(w,0,-1):
        if j>=weights[i]:
            dp[j]=max(dp[j-weights[i]]+values[i],dp[j])
print(dp[-1])