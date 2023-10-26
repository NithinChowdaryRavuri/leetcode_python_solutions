class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace('-','').upper()
        if len(s)<=k:
            return s
        if len(s)%k != 0:
            return s[:len(s)%k] +'-'+ "-".join([s[i:i+k] for i in range(len(s)%k,len(s),k)])
        else:
            return "-".join([s[i:i+k] for i in range(0,len(s),k)])