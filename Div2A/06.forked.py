# Question: https://codeforces.com/problemset/problem/1904/A

# Idea: 
# Created sets for all valid moves for king and all valid points for 
# queen and then taking intersection of that set to get the count of 
# valid positions to place the knight

def getCoords(a, b, x, y):
    s = set()
    s.add((x+a, y+b))
    s.add((x+a, y-b))
    s.add((x-a, y+b))
    s.add((x-a, y-b))
    s.add((x+b, y+a))
    s.add((x+b, y-a))
    s.add((x-b, y+a))
    s.add((x-b, y-a))
    return s

def main():
    t = int(input())
    for _ in range(t):
        a, b = list(map(int, input().split()))
        xk, yk = list(map(int, input().split()))
        xq, yq = list(map(int, input().split()))

        k_set = getCoords(a, b, xk, yk)
        q_set = getCoords(a, b, xq, yq)

        ans = 0

        for item in k_set:
            if item in q_set:
                ans += 1
        
        print(ans)


if __name__ == "__main__":
    main()