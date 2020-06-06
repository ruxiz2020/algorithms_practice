"""
@param s: a list of characters
"""
def reverse(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

ss = ['昨天', 'yesterday', 'tomorrow']
print(ss)
reverse(ss)
print(ss)
