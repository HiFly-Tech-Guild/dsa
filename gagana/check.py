
def is_sort(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
arr = [1, 2, 3, 4, 5]
print( is_sort(arr))  
arr = [5, 3, 4, 1, 2]
print( is_sort(arr)) 

#O(n) 

