def swap(arr, i, j):
  aux = arr[i]
  arr[i] = arr[j]
  arr[j] = aux

def burbuja(arr):
  for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        swap(arr, j, j + 1)
  return arr
    
def busquedaBinaria(arr, n):
    d = len(arr)/2
    
    if arr[d] == n:
        return true
    if arr[d] < n:
        #(arr[d:], n)
        for i in range(len(arr[d:])):
            for j in range(len(arr[]))
        #(arr[:d], n)

arr=burbuja([6, 8, 2, 5, 1, 9])
busquedaBinaria(arr,5)


