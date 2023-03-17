def palindrome(s):
    str = ""
    for i in s:
        str = i + str
    return str

s="MALAYALAM"
y=palindrome(s)
print("reversed string is :",y)

if y==s:
    print(True)
else:
    print(False)



