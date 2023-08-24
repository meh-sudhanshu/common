
def isPalindrome(str):
    if len(str) == 0:
        return True
    if len(str) == 1:
        return True
    if str[0] != str[-1]:
        return False
    sstr = str[1:len(str)-1]
    return isPalindrome(sstr)
print(isPalindrome("Madam"))
