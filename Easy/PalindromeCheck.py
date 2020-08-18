def isPalindromeOne(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return reversedString == string


def isPalindrome(string):
    reversedStr = []
    for i in reversed(range(len(string))):
        reversedStr.append(string[i])
    return string == "".join(reversedStr)
