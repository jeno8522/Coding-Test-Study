n = int(input())
members = []

for _ in range(n):
    age, name = input().split()
    age = int(age)
    members.append((age, name))
members = sorted(members, key= lambda x: x[0])


for person in members:
    print(person[0], person[1])
