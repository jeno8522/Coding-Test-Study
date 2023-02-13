import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    root = result = ListNode(None)
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            #중복값 방지를 위해 index도 따로 저장
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        #pop한 node로 이동
        result = result.next
        #다음 node가 존재하면
        if result.next:
            #다음 node를 heap에 push
            heapq.heappush(heap,(result.next.val,idx,result.next)

        return root.next
