num = [3,5,2,8]
index = 0
result = []
while index < len(num)-1:
    pair = num[index] + num[index+1]
    result = result + [pair]
    index += 1
print(result)
