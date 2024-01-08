class Solution(object):
    def shipWithinDays(self, weights, days):
        def feasible(weights, days, capacity):
            required_days, current_weight = 1, 0
            for weight in weights:
                current_weight += weight
                if current_weight > capacity:
                    required_days += 1
                    current_weight = weight
            return required_days <= days
        if days == 1:
            return sum(weights)
        
        if days == len(weights):
            return max(weights)

        left, right = max(weights), sum(weights)
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if feasible(weights, days, mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result