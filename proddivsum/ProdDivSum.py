# Create a function that takes a list of integers and returns whether the product of those integers is divisible by their sum or not.
# The function should return True if the product of all the integers in the list is divisible by their sum and False otherwise.



def is_product_divisible_by_sum(numbers):
    if not numbers:
        return False
    
    product = 1
    summation = 0

    for num in numbers:
        product *= num
        summation += num

    print(f'Product: {product}, Sum: {summation}')
    if summation == 0:
        return False

    return product % summation == 0