class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        counts = Counter(s)
        pq = [(-value,key) for key,value in counts.items()]
        heapify(pq)
        if -pq[0][0]>(n+1)//2:
            return ''
        res=[None]*n
        pointer=0
        while pq:
            (count,char) = heappop(pq)
            count = -count
            for i in range(count):
                res[pointer]=char
                pointer+=2
                if pointer>=n:
                    pointer=1
        return ''.join(res)