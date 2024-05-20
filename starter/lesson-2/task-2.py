'''
Завдання 2
Напишіть програму, яка запитує три цілі числа a, b і x
та друкує їх добуток.
'''

multiply_result = 1

nums = {
    'a': None,
    'b': None,
    'x': None
}

for k in nums:
    num = input(f"Enter {k}: ")
    # check if not empty
    # in number
    # if integer
    nums[k] = int(num)

for v in nums.values():
    multiply_result *= v

print(multiply_result)
