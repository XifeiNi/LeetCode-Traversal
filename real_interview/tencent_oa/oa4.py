def readIn():
    sizeOfArr = int(input())
    data = map(int, input().strip().split())
    A = []
    A.extend(data)
    data = map(int, input().strip().split())
    B = []
    B.extend(data)
    arr = []
    for i in range(len(A)):
        arr.append([A[i], B[i]])
    bubble(arr)
def bubble(arr):
    n = len(arr) 
    swap = 0
    # Traverse through all array elements 
    for i in range(n): 
        for j in range(0, n-i-1): 

            if arr[j][0] > arr[j+1][0] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arr[j][0], arr[j][1] = arr[j][1], arr[j][0]
                arr[j + 1][0], arr[j+1][1] = arr[j+1][1], arr[j+1][0]
                swap += 1
    print(swap)
readIn()
