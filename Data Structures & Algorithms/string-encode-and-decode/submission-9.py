class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for i in strs:
            string += '#' + str(len(i)) + '#'
            string += i
        return string

    def decode(self, s: str) -> List[str]:
        i = 0
        # print(s)
        lst = []
        if len(s)> 0:
            # i = s[0]
            while i < len(s):
                # print("len: ", s[i])
                j = i+1
                w_len = ''
                # print('j: ', s[j], ' j+1: ', s[j+1])
                while s[j] != '#':
                    w_len += s[j]
                    j += 1 
                # print("i: ", i, "W_len: ",w_len)
                i = j
                w_len = int(w_len)
                lst.append(s[i+1:i+w_len+1])
                i += w_len+1
        return lst
