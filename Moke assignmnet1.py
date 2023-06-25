def moveZeroes(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    while left < len(nums):
        nums[left] = 0
        left += 1
    return nums

arr=[0,1,0,3,12]
print(moveZeroes(arr))


