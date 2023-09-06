import sys

input = sys.stdin.readline

if __name__ == '__main__':
    import sys
    word = input().rstrip()
    for i in range(len(word)):
        if word[i:] == word[i:][::-1]:
            print(len(word) + i)
            break