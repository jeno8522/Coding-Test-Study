from itertools import product
import math
def solution(users, emoticons):
    answer = [0, 0]
    dis_emoticons = []
    for i in range(len(emoticons)):
        tmp = []
        for j in range(10, 41, 10):
            dis = (100 - j)
            dis_price = emoticons[i] * dis / 100
            tmp += [int(dis_price)]
            # print(dis)
            # print(dis_price)
            # print(tmp)
        dis_emoticons.append(tmp)

    # print(dis_emoticons)

    info = []
    for combi in product([0,1,2,3], repeat=len(dis_emoticons)):
        # print(combi)
        total_price = 0
        plus = 0
        for i in range(len(users)):
            idx = math.ceil(users[i][0] / 10) - 1
            price = 0
            for j in range(len(combi)):
                if combi[j] >= idx:
                    price += dis_emoticons[j][combi[j]]
            if price >= users[i][1]:
                plus += 1
            else:
                total_price += price
        info.append([plus, total_price])

    info = sorted(info, key=lambda x:(x[0],x[1]), reverse=True)
    # print(info)
    answer = info[0]
    return answer

# print(solution([[40, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))