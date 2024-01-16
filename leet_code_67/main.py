class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        result = []
        carry = 0
        while a or b:
            temp1 = a.pop() if a else 0
            temp2 = b.pop() if b else 0
            current = carry + int(temp1) + int(temp2)
            if current==0 or current==1:
                result.append(str(current))
                carry = 0
            elif current==2:
                result.append(str(0))
                carry = 1
            else:
                result.append(str(1))
                carry = 1
        if carry:
            result.append(str(1))
        return ''.join(result[::-1])