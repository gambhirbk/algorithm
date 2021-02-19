"""
There are two sorted arrays A[1...n] and B[1...m] of size n and m 
respectively. Design an efficient algorithm to find the kth smallest
number of the two sorted arrays
"""

def k_smallest(arr1, arr2, n, m, k):
    if n > m:
        return k_smallest(arr2, arr1, m, n, k)

    if (n == 0 and m>0):
        return arr2[k-1]
    
    if (k==1):
        return min(arr1[0], arr2[0])

    i = min(n, k//2)
    j = min(m, k//2)

    if arr1[i-1] < arr2[j-1]:
        return k_smallest(arr1[i:], arr2, n-i, j, k-i)

    else:
        return k_smallest(arr1, arr2[j:], i, m-j, k-j)

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9]

print(k_smallest(arr1, arr2, 4, 3, 2))
    
