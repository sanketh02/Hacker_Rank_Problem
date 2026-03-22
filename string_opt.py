if 0 < len(s) < 1000:
    print(any(c.isalnum() for c in s))

    flag = False
    for i in s:
        if i.isalpha():
            flag = True
    print(flag)

    flag = False
    for i in s:
        if i.isdigit():
            flag = True
    print(flag)

    flag = False
    for i in s:
        if i.islower():
            flag = True
    print(flag)

    flag = False
    for i in s:
        if i.isupper():
            flag = True
    print(flag)

# optimize version
s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
