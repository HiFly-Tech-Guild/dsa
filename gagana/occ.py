def count_occurrences(arr, target):
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count
arr = [1, 2, 3, 4, 5, 3, 3, 3,4,3]
target = 3
print(f"Occurrences of {target}:", count_occurrences(arr, target))  
# O(n)