# A magic index in an array A[1...n-1] is defined to be an index such that A[i] == i. 
# Given a sorted array of distinc integers (with a single magic index), write a method to find a magic index, if 
# one exists, in array A

A = [ -30, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
#idx   0    1   2   3  4  5  6  7  8  9   10

def naiveApproach(lst: list):
   for i, e in enumerate(lst):
      if e == i:
         return e 
   
from math import floor

def magicIndex(lst: list):
   mididx = floor(len(lst)/2)
   startidx = 0
   endidx = len(A) -1
   print(f'startidx {startidx}, mididx {mididx}, endidx {endidx}, list {str(lst)}')

   while :
      if lst[index] == index:
         return index
      elif lst[index] < index:
         end
      elif lst[index] > index:
         return magicIndex(lst[:index])
   
