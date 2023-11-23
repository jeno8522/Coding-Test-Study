

if __name__=='__main__':
    str = input()
    s = set()
    for i in range(1, len(str)+1):
        for j in range(len(str) - i+1):
            s.add(str[j:j+i])
    print(len(s))