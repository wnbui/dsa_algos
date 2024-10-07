def sequential(nums: list, value: int) -> bool:
    for num in nums:
        if num == value:
            return True
    
    return False

def sequential_optimization(nums: list) -> int:
    max = nums[0]

    for num in nums:
        if num > max:
            max = nums
    
    return max