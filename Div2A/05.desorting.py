# Question: https://codeforces.com/problemset/problem/1853/A

# Idea: 
# Every operation increases the gap by two at index i and i+1.
# So just find the minimum gap between adjacent values and divide it by 2.
# this division can lead to a tie with equal adjacent numbers, so add 1 in final result.


def solve (arr, n):
    min_gap = float('inf')
    for i in range(n-1):
        gap = arr[i+1]-arr[i]
        # print("==> ",gap)
        if gap < 0:
            return 0
        min_gap = min(min_gap, gap)
    return min_gap // 2 + 1

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr, n))

if __name__ == "__main__":
    main()