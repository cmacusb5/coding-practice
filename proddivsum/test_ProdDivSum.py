from ProdDivSum import *


def test_ProdDivSum():
    input1 = [1, 2 ,3, 4] #24/10 False
    input2 = [1, 1,1, 1, 1] # 1/5 False
    input3 = [5, 7, 8, 9, 10] # True
    input4 = [8] # 8/1 True
    input5 = [] # False
    input6 = [0, 0, 0] # False
    input7 = [2,4,6,8,10] # True
    input8 = ['a', 1.3, 5, 7] # False
    input9 = 'thisis a string'
    input10 = "10,8,9,0"

    assert is_product_divisible_by_sum(input1) == False
    assert is_product_divisible_by_sum(input2) == False 
    assert is_product_divisible_by_sum(input3) == False 
    assert is_product_divisible_by_sum(input4) == True 
    assert is_product_divisible_by_sum(input5) == False
    assert is_product_divisible_by_sum(input6) == False
    assert is_product_divisible_by_sum(input7) == True
    # Bonus Work, Sanitize the input and handle data going into the function
    # that is not an array on integers
    #assert is_product_divisible_by_sum(input8) == False
    #assert is_product_divisible_by_sum(input8) == False
    #assert is_product_divisible_by_sum(input8) == False