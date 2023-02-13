from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    combi = []
    for i in range(1, col + 1):
        combi += (combinations(range(col), i))          # 모든 부분집합(값 대신 인덱스)

    unique = []
    for e in combi: #저장된 인덱스 부분집합
        tmp = [tuple(item[key] for key in e) for item in relation]  #set에 넣기 위해 tuple 사용, combi에 저장된 인덱스에 해당하는 relation의 모든 아이템
        if len(set(tmp)) == len(relation):  #set에 넣어도 길이가 그대로면 중복 없음 -> 유일성
            isUnique = True
            for u in unique:
                if set(u).issubset(set(e)): #이미 후보키가 이번 combi에 저장된 인덱스의 부분집합이면 -> 최소성 위반
                    isUnique = False
                    break
            if isUnique == True:
                unique.append(e)
    return len(unique)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))