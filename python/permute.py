def permute(arr):
    if len(arr) == 0:
        return [[]]
    if len(arr) == 1:
        return [[arr[0]]]
    ans = []
    for i in range(len(arr)):
        temp = [arr[i]]
        sarr = arr[0:i]+arr[i+1:]
        ll = permute(sarr)
        for l in ll:
            ans.append(temp+l)
    return ans

print(permute([1,2,3,4]))
