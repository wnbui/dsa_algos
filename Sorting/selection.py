# In-place selection sort
def selection_short(nums: list):

    for i in range(len(nums) - 2):
        least_index = i
        for j in range(i + 1, len(nums) - 1):
            if nums[j] < nums[least_index]:
                least_index = j
        nums[least_index], nums[i] = nums[i], nums[least_index]


unsorted = [5, 2, 7, 8, 3, 4, 1, 9]

print(unsorted)
selection_short(unsorted)
print(unsorted)