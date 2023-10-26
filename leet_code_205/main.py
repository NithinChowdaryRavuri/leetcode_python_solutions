class Solution(object):
    def isIsomorphic(self, a, b):
        list_a, list_b = [], []
        c, d = "",""
        for i in range(len(a)):
            if a[i] not in list_a:
                list_a.append(a[i])
                c+=str(i)
            else:
                c+=str(list_a.index(a[i]))
            c+="-"
            if b[i] not in list_b:
                list_b.append(b[i])
                d+=str(i)
            else:
                d+=str(list_b.index(b[i]))
            d+="-"
        if c==d:
            return True
        else:
            return False