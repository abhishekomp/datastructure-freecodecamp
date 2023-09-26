def square_numbers(nums):
  result = []
  for i in nums:
    result.append(i*i)
  return result

# my_nums = square_numbers([1,2,3,4,5])
# print(my_nums)



def square_numbers_generator(nums):
  """
  Generator function that takes a number list
  Returns the square of each number
  """
  for i in nums:
    yield (i*i)


# my_nums = square_numbers_generator([1,2,3,4,5])
"""
Converting a generator to a list. Note: You lose the benefits provided by generator when you convert it to a list. 
This is particularly visible with large set of data
"""
# print(list(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# for num in my_nums:
#   print(num)

# List comprehension to achieve the same result
my_nums = [x*x for x in [1,2,3,4,5]]
for num in my_nums:
  print(num)