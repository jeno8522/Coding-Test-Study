def solution(n, build_frame):
    def is_possible() -> bool:
        gidoong, bo = 0, 1
        for c, r, isBo in res:
            if isBo == gidoong:
                if not (r == 0 or (c,r,bo) in res or (c-1,r,bo) in res or (c,r-1,gidoong) in res):
                    return False
            else:
                if not ((c,r-1,gidoong) in res or (c+1,r-1,gidoong) in res or ((c-1,r,bo) in res and (c+1,r,bo) in res)):
                    return False
        return True

    res = set()     #시간 절약을 위해 set 사용
    for c, r, isBo, isInsert in build_frame:
        if isInsert:    #추가
            res.add((c, r, isBo))   #요소를 추가해보고
            if not is_possible():   #불가능한 부분이 있으면
                res.remove((c,r,isBo))  #추가했던 요소 삭제
        elif (c,r,isBo) in res: #삭제
            res.remove((c,r,isBo))  #요소를 삭제해보고
            if not is_possible():   #불가능한 부분이 있으면
                res.add((c, r, isBo))   #삭제했던 요소 추가
    answer = list(map(list, res))   #tuple이 저장되어있는 set을 list화
    answer = sorted(answer, key= lambda x: (x[0],x[1],x[2]))    #정렬


    return answer



build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(5, build_frame))