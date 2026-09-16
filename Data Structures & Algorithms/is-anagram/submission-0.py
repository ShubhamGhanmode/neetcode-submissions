class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}

        for i in s:
            if i in sdict:
                sdict[i] += 1
            else:
                sdict[i] = 1
        for j in t:
            if j in tdict:
                tdict[j] += 1
            else:
                tdict[j] = 1
        if sdict == tdict:
            return True
        else:
            return False