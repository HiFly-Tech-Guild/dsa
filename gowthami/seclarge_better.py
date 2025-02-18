a=[6,3,10,5,3,2]
largest=a[0]
n=len(a)
for i in range(1,n-1):
    if a[i] > largest:
        largest = a[i]
seclarg=-1
for i in range( 0, n-1):
    if a[i] > seclarg and a[i] != largest:
        seclarg= a[i]
print(seclarg)

# O(N + N) = 2N
# since we are traversing the array two types