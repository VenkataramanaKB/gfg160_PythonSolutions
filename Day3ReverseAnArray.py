class Solution:
    def reverseArray(self, arr):
        # code here
       lef = 0
       rig = len(arr)-1
       while lef<rig:
           arr[lef], arr[rig] = arr[rig], arr[lef]
           lef +=1
           rig -=1
           