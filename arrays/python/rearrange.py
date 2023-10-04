from sys import argv

# create a array from the given range
array = [0] * int(argv[1])

# array pointers
array_len = len(array)
array_mid = array_len // 2
array_end = array_len - 1

# populate the array
for i in range(array_len):
    array[i] = i

new_array = [0] * array_len

# populate the new array
count = 0
while count < array_mid:
    left = count
    right = array_end - count

    lpos = count + count
    rpos = lpos + 1

    new_array[lpos] = array[left]

    if left != right:
        new_array[rpos] = array[right]

    count += 1

# assign value for the last item when the array length is odd
if (array_len % 2) == 1:
    new_array[array_end] = array_mid

print(new_array)
