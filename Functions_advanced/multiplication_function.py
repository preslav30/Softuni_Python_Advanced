def multiply(*nums):
    result = 1
    for i in range(len(nums)):
        result *= nums[i]
    return result

