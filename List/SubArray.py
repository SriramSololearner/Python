arr = [1, 2, 3, 4, 5]

# Find all subarrays
for i in range(len(arr)):
    for j in range(i, len(arr)):
        subarray = arr[i:j+1]
    print(subarray)