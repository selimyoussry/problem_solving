# solution.py

"""

function getAnotherNumber(arr):
   n = length(arr)
   if (n == MAX_INT+1): # all non-negative integers are in arr
      return null
   arr2 = []
   for i from 0 to n:
      arr2[i] = 0
   for i from 0 to n-1:
      num = arr[i]
      arr2[num % (n+1)] = 1
   for i from 0 to n:
      if arr2[i] == 0:
         return i


function getAnotherNumber(arr):
   n = length(arr)
   if (n == MAX_INT+1): # all non-negative integers are in arr
      return null
   arrMap = Array[n+1]
   for i from 0 to n:
      arrMap[arr[i]] = 1

   for j from 0 to n:
      if (arrMap[j] == 0):
         return j

"""