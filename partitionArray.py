# 快慢指针

def partitionArray(nums):
    # write your code here
    index = 0
    for i in range(0, len(nums)):
        print('i')
        print(i)
        if nums[i] & 1:
            print('index')
            print(index)
            print(nums)
            nums[index], nums[i] = nums[i], nums[index]
            index += 1


ar = [1, 5, 3, 8]

print(ar)
partitionArray(ar)
print(ar)
