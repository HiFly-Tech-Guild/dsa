a=[1,2,2,2,2,2,2]
a.sort()
print(a)
n=len(a)
largest=a[n-1]
for i in range(n-2,-1,-1):
    if a[i] != largest:
        seclarg=a[i]
        break;
else:
    seclarg=None
print(seclarg)
#n log n + N
