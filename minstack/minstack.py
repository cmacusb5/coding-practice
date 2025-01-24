class MinStack:
   def __init__(self):
      self.s1 = []
      self.minimum = []

   def push(self, value):
      self.s1.append(value)
      if (self.minimum == []) or (value < self.minimum[-1]):
         self.minimum.append(value)
      else:
         self.minimum.append(self.minimum[-1])
   
   def pop(self, value):
      self.minimum.pop()
      return self.s1.pop()
      
   
   def min(self):
      return self.minimum[-1]
   

