def isPalindrome(head):
    rev = None
    slow = fast = head

    #runner 기법을 이용해 중간지점 까지의 연결리스트의 역순인 연결리스트 rev 생성
    while fast and fast.next:   #전체 리스트의 갯수가 짝수일 경우 마지막에 fast가 none, 홀수일 경우 fast.next가 none
        fast = fast.next.next #두 칸 씩 전진
        rev, rev.next, slow = slow, rev, slow.next #다중할당기법으로 두줄이상으로 나눠 적었을 때와 차이점이 있음. (다중할당은 동시에 현재 값을 기준으로 처리)
        #while문은 연결리스트의 중간지점에서 종료됨, rev는 중간지점 전의 연결리스트의 역순인 연결리스트로 생성됨

    if fast :   #연결리스트의 갯수가 홀수일 경우 while문이 끝난 뒤 fast는 연결리스트의 마지막요소를 가리킴
        slow = slow.next    #이 경우 slow는 홀수 개인 연결리스트의 중간 지점이므로 palindrome check가 필요 없는 지점에 위치
                            #한 칸 전진이 필요하다. (rev는 중간 지점 전까지 생성되었기도 했으므로)

    while slow and rev: #slow와 rev 비교
        if slow.val != rev.val:    #다르면 palindrome 실패
            return False
        slow, rev = slow.next, rev.next

    return True