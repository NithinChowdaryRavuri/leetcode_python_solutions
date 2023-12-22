class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(word):
            return word==word[::-1]
        def dfs(start_index, cur_path):
            if start_index == n:
                res.append(cur_path)
                return
            for end in range(start_index+1, n+1):
                prefix = s[start_index:end]
                if is_palindrome(prefix):
                    dfs(end, cur_path+[prefix])

        res = []
        n = len(s)
        dfs(0, [])
        return res
        