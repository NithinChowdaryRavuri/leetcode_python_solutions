class Solution(object):
    def addStrings(self, num1, num2):
        i, j, carry, result = len(num1) - 1, len(num2) - 1, 0, []

        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            temp_sum = n1 + n2 + carry
            carry = temp_sum // 10
            result.append(str(temp_sum % 10))

            i -= 1
            j -= 1

        return ''.join(result[::-1])