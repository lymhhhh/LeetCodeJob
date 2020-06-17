def sort(A):
    for i in range(0,len(A)):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

print(sort([4,5,1,3,2]))