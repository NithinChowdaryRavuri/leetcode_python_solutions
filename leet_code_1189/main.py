class Solution(object):
    def maxNumberOfBalloons(self, text):
        char_counts = Counter(text)
        count = char_counts['b']
        for char in 'balloon':
            if char in 'lo':
                count = min(count, char_counts[char] // 2)
            else:
                count = min(count, char_counts[char])

        return count