def find_ways(n):
    if n==0 or n==1:
        return 1
    return find_ways(n-1)+find_ways(n-2)

print(find_ways(3))