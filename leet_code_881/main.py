class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people)-1
        result = 0
        while i<=j:
            result+=1
            if people[i]+people[j]<=limit:
                i+=1
            j-=1
        return result