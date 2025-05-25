# Question: https://codeforces.com/problemset/problem/1777/A

# Idea:
# observe that the given operation is equivalent to selecting two equal parity 
# adjancent elements and deleting one of them.

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        counter = 0
        for i in range(len(arr)-1):
            a = arr[i]
            b = arr[i+1]
            if a%2 == b%2:
                counter += 1
        print(counter)


if __name__ == "__main__":
    main()