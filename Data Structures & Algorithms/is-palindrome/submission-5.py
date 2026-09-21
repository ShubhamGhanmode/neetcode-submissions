class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip = s.lower()
        i = 0
        j = len(strip)-1
        while True:
            if j <= i:
                print('breaks?')
                break
            while strip[i].isalnum() != True and i < len(strip)-1:
                i += 1
            while strip[j].isalnum() != True and i < len(strip)-1 :
                j -= 1
            if strip[i] == strip[j]:
                print('SAME: ',strip[i],strip[j])
                i += 1
                j -= 1
                continue
            else:
                print('Not SAME???: ',strip[i],strip[j])

                return False

        return True