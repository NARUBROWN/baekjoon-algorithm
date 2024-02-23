def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


n = int(input())

for _ in range(n):
    text = input().lower()
    if isPalindrome(text):
        print("Yes")
    else:
        print("No")
