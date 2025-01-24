from minstack import MinStack

def test_minstack():
   m = MinStack()
   m.push(3)
   assert m.min() == 3
   m.push(7)
   assert m.min() == 3
   m.push(2)
   assert m.min() == 2