class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom)//2
            # print(mid)
            if matrix[mid][-1] > target and matrix[mid][0] > target:
                bottom = mid-1
            elif matrix[mid][-1] < target and matrix[mid][0] < target:
                top = mid+1
            else:
                row = matrix[mid]
                i = 0
                j = len(row)-1
                # print(i,j)
                while i <= j:
                    m = (i+j)//2
                    # print(m)
                    if row[m] < target:
                        i = m+1
                    elif row[m] > target:
                        j = m-1
                    else:
                        return True
                return False

        return False
        