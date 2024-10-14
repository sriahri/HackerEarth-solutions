def caseConversion(s):
    # Write your code here that converts the given camel case string s  and
    # returns a snake case version of that string
    x = ''
    x += s[0].lower()
    for i in s[1:]:
        if i.isupper():
            x += '_'
            x += i.lower()
        else:
            x += i
    return x


T = int(input())
for _ in range(T):
    s = input()

    out_ = caseConversion(s)
    print(out_)
