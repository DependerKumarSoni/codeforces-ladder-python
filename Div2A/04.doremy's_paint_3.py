# Question: https://codeforces.com/problemset/problem/1890/A

# Idea: Iterate through the array and count the occurrences of each distinct number using map.
# Check the following case 1. If there are only one or two distinct elements in the array then
# it's possible to rearrange the array. 2) If there is only one distinct element , then answer
# is Yes because all the elements are already the same. 3) If there are two distinct elements,
# check if one of them appears exactly n/2 times. If so it is possible to rearrange the array 
# to meet the conditions. If there are three of more distinct elements, it is not possible to 
# rearrange the array to meet the condition.

from collections import Counter
 
def solve (arr, n):
    s = set(arr)
    if len(s) == 1:
        return "YES"
    elif len(s) == 2:
        c = Counter(arr)
        for val in c.values():
            if (n%2 == 0 and val == n//2) or (n%2 != 0 and (val == n//2 or val == n//2+1)):
                return "YES"
            else:
                return "NO"
    else:
        return "NO"
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr, n))
 
if __name__ == "__main__":
    main()
