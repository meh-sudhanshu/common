

def findSum(arr,k):
    i = 0
    j = k-1
    ans = 0
    ps = 0
    while j<len(arr):
        if i == 0:
            csum = sum(arr[i:j+1])
            ans = csum
            ps = csum
            i+=1
            j+=1
        else:
            csum = ps - arr[i-1] + arr[j]
            if csum > ans:
                ans = csum
            ps = csum
            i+=1
            j+=1
    return ans

