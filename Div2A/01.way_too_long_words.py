# Question: https://codeforces.com/problemset/problem/71/A

# Idea: For each word , determine its length L and check if it's greater than 10.
# If it is output the word as it. Otherwise construct abbreviation by the given rules : 
# first letter of the word followed by L - 2 , and finally the last letter of the word.

def solve (word):
    if len(word) <= 10:
        print(word)
    else:
        print(f'{word[0]}{len(word)-2}{word[-1]}')

def main():
    t = int(input())
    for _ in range(t):
        word = input()
        solve(word)


if __name__ == "__main__":
    main()