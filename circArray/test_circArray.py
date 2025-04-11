from circArray import *

def test_list():
   i1 = [1, 2, 3]
   iterations = 0
   for i in i1:
      print(i)
      iterations += 1
   assert iterations == 3

def test_iterable():
   i1 = CircularArray(10)
   length = sum(1 for i in i1)
   
   iterations = 0
   for i in i1:
         print(i)
         iterations += 1
   assert iterations == length

