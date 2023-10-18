class Solution(object):
    def letterCombinations(self, digits):
        result = [""]
        if digits == '':
            return []
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        for digit in digits:
            letters = d[digit]
            temp = []
            for prev in result:
                for letter in letters:
                    temp.append("".join([prev, letter]))
            result = temp
        return result