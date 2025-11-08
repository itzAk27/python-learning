s = "aKHTAR"

l = list(s)
print(l)

print(s[0].islower())

if s[0].islower():
    l[0] = s[0].upper()
    print(l)