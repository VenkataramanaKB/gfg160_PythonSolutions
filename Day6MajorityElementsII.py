class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        num = len(arr)//3
        d = {}
        lis = []
        for i in arr:
            d[i] = 1+d.get(i,0)
        for i, n in d.items():
            if n > num:
                lis.append(i)
        lis.sort()
        return lis