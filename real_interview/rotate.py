
# 单调递增序列
# 找任意一个位置分成两段
# 平移

class RotatedSortedArray:
    def searchMaximumInRotatedSortedArray(self, array):
        if array is None or len(array) == 0:
            return -1
        start , end = 0,  len(array) - 1
        if array[start] < array[end]:
            return array[end]
        while start + 1 < end:
            mid = (start + end ) // 2
            if array[mid] < array[end]:
                end = mid
            elif array[mid] == array[end]:
                if array[mid] > array[start]:
                    start = mid
                elif array == array[start]:
                    return max(array[start: end])
                else:
                    end = mid
            else:
                start = mid
        
        return max(array[start], array[mid])

rotated = RotatedSortedArray()
test1 = []
test2 = [4, 5, 6, 7, 1, 2, 3]
test3 = [3, 4, 5, 1, 2]
test4 = None
test5 = [5, 6, 7, 1, 2]
test6 = [1, 2, 3, 5, 6]
test7 = [5, 6, 6, 7, 7, 1, 2]
test8 = [1, 1, 1, 1, 1]
test9 = [4, 4, 4, 1, 2, 3, 4]
test10 = [4, 2, 4, 4, 4]
test11 = [4, 4, 4, 2, 4]
print(rotated.searchMaximumInRotatedSortedArray(test1))
print(rotated.searchMaximumInRotatedSortedArray(test2))
print(rotated.searchMaximumInRotatedSortedArray(test3))
print(rotated.searchMaximumInRotatedSortedArray(test4))
print(rotated.searchMaximumInRotatedSortedArray(test5))
print(rotated.searchMaximumInRotatedSortedArray(test6))
print(rotated.searchMaximumInRotatedSortedArray(test7))
print(rotated.searchMaximumInRotatedSortedArray(test8))
print(rotated.searchMaximumInRotatedSortedArray(test9))
print(rotated.searchMaximumInRotatedSortedArray(test10))
print(rotated.searchMaximumInRotatedSortedArray(test11))
