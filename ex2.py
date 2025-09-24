from bisect import bisect_left, bisect_right

def countBetween(arr, low, high):
    arr.sort()
    ans = []
    for l, h in zip(low, high):
        left = bisect_left(arr, l)
        right = bisect_right(arr, h)
        ans.append(right - left)
    return ans
