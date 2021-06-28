string1 = "aabbcce"
string2 = "aabbcced"

def common(a,b):
    a = a.lower()
    b = b.lower()
    c = ""
    for item in a:
        if item in b:
            if item not in c:
                c = c + item
    d = ''.join(sorted(c))
    return d

print(common(string1,string2))
