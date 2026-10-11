class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxp = max(piles)
        i = 1
        j = maxp
        final = 0

        while i <= j:
            m = (i + j) // 2
            count = 0
            for p in piles:
                count += p // m
                if p % m != 0:
                    count +=1
            if count > h:
                i = m + 1
            elif count <= h:
                j = m - 1
                final = m
        return final

