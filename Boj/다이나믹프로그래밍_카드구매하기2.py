n = int(input())
ps = list(map(int, input().split()))
ps = [0] + ps

dp = [999999999 for i in range(1001)]
dp[0] = 0

for i in range(n + 1):
    for j in range(i + 1):
        dp[i] = min(dp[i], ps[j] + dp[i - j])

print(dp[n])