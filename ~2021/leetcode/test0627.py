keyboard = ["가","호","저"],["알","크","청"],["개","캠","산"]

def solution(word):
    answer = []
    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1
    l = 1000
    tmp = 0
    cnt = 0
    s = 0

    for k in range(len(word)-1):
        x1 = -1
        y1 = -1
        x2 = -1
        y2 = -1
        l = 1000
        tmp = 0
        for i in range(len(keyboard)):
            for j in range(len(keyboard)[i]):
                if word[k] == keyboard[i][j]:
                    x1 = i
                    y1 = j
                    if x1 >= 0 and x2 >= 0 and y1 >= 0 and y2 >= 0:
                        tmp = (x1 - x2) + (y1 - y2)
                        if tmp < 0:
                            tmp = -tmp
                if word[k+1] == keyboard[i][j]:
                    x2 = i
                    y2 = j
                    if x1 >= 0 and x2 >= 0 and y1 >= 0 and y2 >= 0:
                        tmp = (x1 - x2) + (y1 - y2)
                        if tmp < 0:
                            tmp = -tmp
            if tmp < l:
                l = tmp
        if l == 1000:
            s = s + 20
        else:
            s = s + l
            cnt = cnt + 1
print(len(a))
print(len(a[0]))

