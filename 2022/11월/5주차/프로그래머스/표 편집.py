N = 10 ** 9


class Node:
    survived = True

    def __init__(self, p, n):
        self.prev = p if p >= 0 else None
        self.next = n if n < N else None


def solution(n, k, command):
    global N
    N = n
    table = {i: Node(i - 1, i + 1) for i in range(n)}
    current = k
    removed = []

    for cmd in command:
        if cmd == "C":  # 삭제
            table[current].survived = False
            removed.append(current)

            prev, next = table[current].prev, table[current].next
            # 앞 노드의 next를 뒷 노드에 연결
            if prev is not None: table[prev].next = table[current].next
            # 뒷 노드의 prev를 앞 노드에 연결
            if next is not None: table[next].prev = table[current].prev

            # 노드 제거
            if table[current].next is None:  # 다음 노드가 없음
                current = table[current].prev
            else:  # 다음 노드가 있음
                current = table[current].next

        elif cmd == "Z": # 실행 취소
            recovered = removed.pop()
            table[recovered].survived = True

            # 앞 노드의 next를 자신으로 연결
            prev, next = table[recovered].prev, table[recovered].next
            if prev is not None: table[prev].next = recovered
            # 뒤 노드의 prev를 자신으로 연결
            if next is not None: table[next].prev = recovered


        else:
            c, amount = cmd.split()
            if c == "U":
                # 위로
                for _ in range(int(amount)):
                    current = table[current].prev

            elif c == "D":
                # 아래로
                for _ in range(int(amount)):
                    current = table[current].next
    return ''.join(["O" if table[i].survived else "X" for i in range(n)])