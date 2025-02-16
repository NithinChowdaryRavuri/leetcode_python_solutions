class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        len_seq = 2 * n - 1
        seq = [0] * len_seq
        used = [False] * (n + 1)

        def backtrack(i):
            if i == len_seq:
                return True
            if seq[i]:
                return backtrack(i + 1)

            for num in range(n, 0, -1):
                if used[num]:
                    continue
                nxt = i + num if num > 1 else i
                if nxt >= len_seq or seq[nxt] != 0:
                    continue
                seq[i] = seq[nxt] = num
                used[num] = True
                if backtrack(i + 1):
                    return True
                seq[i] = seq[nxt] = 0
                used[num] = False
            return False

        backtrack(0)
        return seq
