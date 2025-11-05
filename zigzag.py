a = ['1','3','5','7']
b = ['2','4','6','8']
count = len(a)
result = ""
i = 0
while i < count:
    result = result + a[i]
    result = result + b[i]
    i = i + 1
print(result)


