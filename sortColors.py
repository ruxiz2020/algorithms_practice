def sortColors(nums):
    # write your code here
    cnt_map = {0: 0, 1: 0, 2: 0}
    for n in nums:
        cnt_map[n] += 1

    i = 0
    for n in (0, 1, 2):
        for j in range(0, cnt_map[n]):
            nums[i] = n
            i += 1


arr = [1, 0, 1, 2]
print(arr)
sortColors(arr)
print(arr)
