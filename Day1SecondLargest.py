class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest = -1
        secondLargest = -1
        for i in range(len(arr)):
            if arr[i]>largest:
                largest = arr[i]
        for i in range(len(arr)):
            if arr[i]>secondLargest and arr[i]!= largest:
                secondLargest = arr[i]
        return secondLargest