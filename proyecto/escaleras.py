def climb_stairs(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
   
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1

    # Fill dp array for all steps
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[N]

print(climb_stairs(6))