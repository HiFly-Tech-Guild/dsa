a=[5,3,2,4,10,2,3,6,6,3,10,7]
large=a[0]
seclarge=-1
n=len(a)
for i in range(0,n):
    if a[i] > large:
        seclarge = large
        large = a[i]
    elif a[i] < large and a[i] > seclarge:
        seclarge = a[i]
print(seclarge)

# def secondSmallest(arr, n):
#     if (n < 2):
#         return -1
#     small = float('inf')
#     second_small = float('inf')
#     for i in range(n):
#         if (arr[i] < small):
#             second_small = small
#             small = arr[i]
#         elif (arr[i] < second_small and arr[i] != small):
#             second_small = arr[i]
#     return second_small

# O(n) traversing the array once