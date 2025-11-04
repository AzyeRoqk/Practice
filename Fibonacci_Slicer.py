#Challenge: "Fibonacci Slicer"
word = "HELLOWORLD"
a, b = 1,1
count = 0
result = ""
while word != "":
    chunk = word[:a]
    word =  word[a:]
    a,b = b, a+b
    if count % 2 != 0:
        reverse = chunk[::-1]
        result = result + reverse
    else:
        result = result + chunk
    count = count + 1
print(result)
