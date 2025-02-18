from typing import List
def sort(a : List[int]) -> int:
    a.sort()
    return a[-1]
if __name__=="__main__":
    a=[1,3,4,2,5,6,3]
    print(sort(a))

# a=[3,4,7,10,2,66]
# a.sort()
# n=len(a)
# print(a[n-1])

# O(n log n) because we are sorting