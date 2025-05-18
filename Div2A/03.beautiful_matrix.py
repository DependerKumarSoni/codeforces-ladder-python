# Question: https://codeforces.com/problemset/problem/263/A

# Idea:
# Calculate the manhattan distance between the position of the number 1 in the matrix and
# the position of the center cell , which is at the interesection of third row and third column.

def solve (mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                return abs(i-2) + abs(j-2)

def main():
    mat = []
    for _ in range(5):
        row = list(map(int, input().split()))
        mat.append(row)
    ans = solve(mat)
    print(ans)

if __name__ == "__main__":
    main()