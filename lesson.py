def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 示例用法
arr = [4, 19, 12, 7, 1]
target = 7
index = linear_search(arr, target)
print("Element", target, "found at index", index)
