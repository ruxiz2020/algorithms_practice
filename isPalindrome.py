def isPalindrome(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            print(i, j)
            return False
        i += 1
        j -= 1
    return True

ss = ['昨天', '昨天', '昨天']
print(ss)
print(isPalindrome(ss))

ss = ['昨天', '前天', '前天', '昨天']
print(ss)
print(isPalindrome(ss))
