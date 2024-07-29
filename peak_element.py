from array import *
#n =  print(" size of array")

arr = array('i', [10,20,30,40,50])

n = len(arr)

if n == 0:
    print("none")

if n == 1:
    print(arr[0])
    
if arr[0] > arr[1]:
    print(arr[0])
    
if arr[n-1] > arr[n-2]:
    print(arr[n-1])

for i in range(1, n-1):
            if arr[i-1] <=  arr[i] and arr[i] >= arr[i+1]:
                print(arr[i])