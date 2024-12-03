class Solution:
    def getMinDiff(self, arr,k):
        # code here
        arr.sort()
        n = len(arr)
        diff = arr[n - 1] - arr[0]
        result = diff
        
        for i in range(n - 1):
            max_height = max(arr[i] + k, arr[n - 1] - k)
            min_height = min(arr[0] + k, arr[i + 1] - k)
            
            if min_height < 0:
                continue
            
            
            result = min(result, max_height - min_height)
        
        return result