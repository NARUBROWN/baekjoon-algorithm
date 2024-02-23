def isPalindrome(s: int) -> bool:
    str_list = str(s).zfill(len(str(s)))
    print(str_list)
    left, right = 0, len(str_list) - 1
    while left < right:
        if str_list[left] != str_list[right]:
            return False
        left += 1
        right -= 1
    return True


n = int(input())

count = 0
while not isPalindrome(n):
    n += 1
    count += 1

print(count)
