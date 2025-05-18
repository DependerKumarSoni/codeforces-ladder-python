# Question: https://codeforces.com/problemset/problem/1903/A

# Idea:
# Check if the array is sorted or if k > 1 , which allows for swapping consectutive elements.
# If either of these conditions is met, then it's always possible to sort the boxes. Otherwise
# it's impossible.

def solve (arr, k):
    if (k > 1 or sorted(arr) == arr):
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        solve(arr, k)

if __name__ == "__main__":
    main()
