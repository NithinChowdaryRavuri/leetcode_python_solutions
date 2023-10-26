class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        r,i,j, sum = 0, 0, 0, 0
        while j<len(arr):
            sum+=arr[j]
            if j-i+1<k:
                j+=1
            else:
                if (sum/k)>=threshold:
                    r+=1
                sum-=arr[i]
                i+=1
                j+=1
        return r