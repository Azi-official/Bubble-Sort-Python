def bubble_sort(arr):
    n = len (arr)
    for i in range (n-1):
        for j in range(n-i-1):
            if arr[j] > arr [j + 1]:
                arr[j] , arr[j +1] = arr [j+1], arr [1]
                return arr

data = [5,3,8,4,2]
print("original list:" , data )

sorted_data = bubble_sort(data)
print("Sorted List:", sorted_data)
