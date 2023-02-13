def textQueries(sentences, queries):
    # Write your code here
    s = []
    q = []
    value = {}
    res = []

    for i in range(len(sentences)):
        s.append(sentences[i].split(' '))
    print(s)
    for i in range(len(queries)):
        q.append(queries[i].split(' '))
    print(q)

    for i in range(len(q)):
        for j in range(len(sentence)):
            if q[i][j] in sentences[j]:
                value.setdefault(q[i][j], 0)
                value[q[i][j]] += 1
        value_tmp = min(value.values())
        # print(tmp)
        tmp = []
        for k in range(value_tmp):
            tmp.append(i)
        res.append(tmp)

    return res

sen = ["bob like alice", "bob kill alice like","abc ab ac bb cc"]
que = ['bob alice', 'like', 'abc']
a = textQueries(sen,que)
print(a)