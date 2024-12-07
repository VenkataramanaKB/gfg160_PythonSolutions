def circularSubarraySum(arr):
    total, maxSum, curMax, minSum, curMin = 0, arr[0], 0, arr[0], 0
    for a in arr:
        curMax = max(curMax + a, a)
        maxSum = max(maxSum, curMax)
        curMin = min(curMin + a, a)
        minSum = min(minSum, curMin)
        total += a
    return max(maxSum, total - minSum) if maxSum > 0 else maxSum