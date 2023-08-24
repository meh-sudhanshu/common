
def find_maxmimum_subarray_sum(arr):
    ans = float('-inf')
    cs = arr[0]
    for i in range(1,len(arr)):
        if cs < 0:
            cs = 0
        if arr[i] <0:
            ans = max(ans,cs)
        cs += arr[i]
        
    return max(cs,ans)
        