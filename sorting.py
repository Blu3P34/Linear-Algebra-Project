arr = [3.14, 2.29, 12,9, 3.14]
new_arr = sorted(arr)
print(new_arr)
for ele in range(1,len(arr)):
    if new_arr[ele] == new_arr[ele - 1]:
        print(new_arr[ele])
