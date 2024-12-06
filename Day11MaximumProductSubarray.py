
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
            res=max(arr)
            currMax,currMin=1,1
            for i in range(len(arr)):
                if arr[i] < 0:
                    currMax,currMin=currMin,currMax
                currMax=max(arr[i]*currMax,arr[i])
                currMin=min(arr[i]*currMin,arr[i])
                res=max(res,currMax)
            return res