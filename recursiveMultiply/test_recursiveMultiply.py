from recursiveMultiply import *

def test_naive_impl():
   assert naive_impl(2, 3) == 6
   assert naive_impl(1000000, 1000000) == 1000000000000

def test_smart_answer():
      assert minProd(2,3) == 6
      assert minProd(1000000, 1000000) == 1000000000000

def test_memo_answer():
   assert memoProd(2,3) == 6
   assert memoProd(1000000, 1000000) == 1000000000000