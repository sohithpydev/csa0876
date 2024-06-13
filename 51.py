from collections import deque
def is_palindrome(x):
    d = deque(x)
    while len(d) >1:
        if d.popleft()!= d.pop():
            return False
    return True
print(is_palindrome("MADAM"))