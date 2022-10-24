from collections import defaultdict

def solution(genres, plays):
    def sort_genres():  #genres 재생 횟수 순으로 sort
        dict_genres = defaultdict(int)

        for i in range(len(genres)):
            dict_genres[genres[i]] += plays[i]
        # dict_genres = sorted(dict_genres, key=lambda x: x[1], reverse=True)
        # dict 자체를 정렬시 key를 기준으로만 정렬, 이 경우에는 key의 인덱스 1에 해당하는 부분으로 정렬하는 셈
        dict_genres = sorted(dict_genres.items(), key=lambda x: x[1], reverse=True)
        # dict.items() 로 인자가 key와 value가 있는 상태에서 x[1]을 선택해줘야 value 기준 정렬이 됨
        return [x[0] for x in dict_genres]

    answer = []

    sorted_genres = defaultdict.fromkeys(sort_genres())   #genres 재생 횟수 순으로 sort한 list
    info_genres = defaultdict(list)     #value가 list인 dict 선언

    for i in range(len(genres)):
        info_genres[genres[i]].append([i, plays[i]])    #dict에 [index, 재생횟수] 저장

    for genre, info in info_genres.items():             #[index, 재생횟수]를 재생횟수 기준 내림차순 후 고유번호(인덱스) 기준 오름차순 정렬
        info_genres[genre] = sorted(info, key=lambda x:(x[1], -x[0]), reverse=True)

    for genre in sorted_genres:     #재생 횟수 순으로 내림차순 정렬한 장르들
        cnt = 0
        for info in info_genres[genre]:     #위의 장르 순으로 info_genres에 접근해 한 장르당 두 개의 재생횟수 많은 곡의 인덱스를 뽑아냄
            answer.append(info[0])
            cnt += 1
            if cnt == 2: break

    # print(info_genres)


    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))