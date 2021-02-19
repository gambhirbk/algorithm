"""
Given a sorted array of distinct integers A[1...n], you want to find out whether
there is an idex i for which A[i] = i
"""
def findIndex(arr):
    l=0
    r=len(arr)
    return binarySearch(arr, l, r-1)

def binarySearch(arr, l, r):
    if r >= l:
        mid = (l+r)//2
    else:
        return -1
    if mid is arr[mid]:
        return mid
    if mid > arr[mid]:
        return binarySearch(arr, (mid+1), r)
    else:
        return binarySearch(arr, l, (mid-1))



print(findIndex([-1, 0, 1, 2, 5, 6]))