n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
solve = []

def dfs(depth):
    if depth == m:
        print(' '.join(map(str, solve)))
        return

    for i in range(n):
        if depth == 0 or solve[depth - 1] <= nums[i]:
            solve.append(nums[i])
            dfs(depth + 1)
            solve.pop()

dfs(0)