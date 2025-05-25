# Question: https://codeforces.com/problemset/problem/1380/A

# Idea:
# oIf there exists such a triple of indices , we can find an index j where 
# aj > aj - 1 and aj > aj + 1. We only need to check n - 2 consecutive triples.

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        found = False
        for j in range(1, n-1):
            i = j - 1
            k = j + 1
            
            if arr[j] > arr[i] and arr[j] > arr[k]:
                print("YES")
                print(i+1, j+1, k+1)
                found = True
                break

        if not found:
            print("NO")

if __name__ == "__main__":
    main()