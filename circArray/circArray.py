# Implement a CircularArray class that supports an array-like data structure which 
# can be efficiently rotated. The class should be iterable.

class CircularArray:
   def clear(self):
      self.iterable = [None] * self.ringSize
   
   def __init__(self, size: int):
      self.ringSize = 10
      self.clear()
      self.readIdx = 0
      self.writeIdx = 0

   def _incrementWriteIdx(self, dir : int): #dir(ection): +1 for incrementing forward by 1, +2 for forward by 2, -1 for backwards by 1, etc
      self.writeIdx += dir
      if self.writeIdx >= self.ringSize:
         self.writeIdx = 0
      elif self.writeIdx < 0:
         self.writeIdx = self.ringSize - 1
      print(f'self.writeIdx = {self.writeIdx}')

   def push(self, a):
      self.iterable[self.writeIdx] = a
      self._incrementWriteIdx(+1)

   def pop(self):
      item = self.iterable[self.writeIdx]
      self.iterable[self.writeIdx] = None
      self._incrementWriteIdx(-1)

   def __iter__(self):
      self.readIdx = 0
      return self
   
   def __next__(self):
      if (self.readIdx < len(self.iterable)):
         item = self.iterable[self.readIdx]
         self.readIdx += 1
         return item
      else:
         raise StopIteration
      
def printIter(i):
   for x in i:
      print(x)