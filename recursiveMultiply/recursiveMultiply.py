# Write a recursive function to multiply two positive integers without using the * 
# operator (or / operator). You can use addition/sutraction, and bit shifting but 
# you should minimize the number of those operations.

def naive_impl(a: int, b: int):
   ret = 0
   for x in range(a):
      ret += b
   return ret

def minProductHelper(smaller: int, bigger: int):
   if smaller == 0:
      return 0
   elif smaller == 1:
      return bigger
   
   # compute half
   s = smaller >> 1
   side1 = minProductHelper(s, bigger)
   side2 = side1
   if smaller % 2 == 1:
         side2 = side1 + bigger
   return side1 + side2

def minProd(a: int, b: int):
   bigger = ( b if a < b else a)
   smaller = (a if a < b else b)
   return minProductHelper(smaller, bigger)

memo = {}

def memoProdHelper(smaller: int, bigger: int):
   global memo
   print(f"before: {memo}")

   if smaller == 0:
      return 0
   elif smaller == 1:
      return bigger
   elif memo.get(smaller, None) != None:
      return memo[smaller]
   print(f"mid: {memo}")

   # compute half
   s = smaller >> 1
   side1 = memoProdHelper(s, bigger)
   print(f"mid2: {memo}")
   side2 = side1
   if smaller % 2 == 1:
         side2 = side1 + bigger
   memo[smaller] = side1 + side2
   print(f"after: {memo}")
   return memo[smaller]

def memoProd(a: int, b: int):
   bigger = ( b if a < b else a)
   smaller = (a if a < b else b)

   return memoProdHelper(smaller, bigger)
