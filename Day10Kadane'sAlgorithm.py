class solution:
     def maxSubArraySum(self,arr):
          result = arr[0]
          maxi = arr[0]
          for i in range(1,len(arr)):
                maxi = max(arr[i]+maxi, arr[i])
                result = max(maxi,result)
          return result