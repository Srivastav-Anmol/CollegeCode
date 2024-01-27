def reverseString(str):
    if len(str)==0:
        return str
    else:
        return reverseString(str[1:])+str[0]
print(reverseString("abcde"))