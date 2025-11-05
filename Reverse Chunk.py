nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
start = 0
result = []
while start < len(nums):
    chunk = nums[start:start+n]
    reverse_chunk = chunk[::-1]
    result = result + reverse_chunk
    start = start + n
print(result)

