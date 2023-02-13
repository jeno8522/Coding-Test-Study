
def dailyTemperatures(temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        #res 0으로 초기화
        res = [0 for i in range((len(temperatures)))]

        #stack을 temperatures의 index를 저장하는 용도로 사용
        for i, e in enumerate(temperatures):
                #새로 참조하는 원소가 stack의 top보다 크면(따뜻하면) and stack에 원소가 존재하면
                while stack and e > temperatures[stack[-1]]:
                        #last에는 stack의 top의 index를 저장해서 res의 해당 index에 새로들어온 원소의 index와 last의 차를 저장
                        #따뜻해지기 전까지 걸린 기간
                        last = stack.pop()
                        res[last] = i - last
                stack.append(i)

        return res


a = [73,74,75,71,69,72,76,73]
r = dailyTemperatures(a)
print(r)

