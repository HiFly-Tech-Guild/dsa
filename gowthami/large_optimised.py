arr=[6,3,10,5,3,2]

def largest(arr: list, n: int) -> int:
    largest=arr[0]
    for i in range(0,n):
        if arr[i]>largest:
            largest=arr[i]
    return largest

print(largest(arr,len(arr)))

# O(n) -> Time Complexity
# O(n) -> Space complexity