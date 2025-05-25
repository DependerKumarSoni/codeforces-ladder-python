# Question: https://codeforces.com/problemset/problem/1761/A

# Idea: 
# After fixing prefix and suffix, it is only possible to perform permutations 
# if we are left with at least two elements in center (except prefix and suffix)
# edge case when n == a == b, it is always considered Yes.

def main():
    t = int(input())
    for _ in range(t):
        n, a, b = list(map(int, input().split()))
        if n == a == b:
            print("Yes")
            continue
        print("Yes") if a+b < n-1 else print("No")

if __name__ == "__main__":
    main()