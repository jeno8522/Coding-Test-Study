import random

#특정수의 인원이 모였을 때 생일이 겹치는 인원이 나올 확률 계산

TRIALS = 100000 #10만번의 실험
same_birthdays = 0  #생일이 같은 실험의 수

for _ in range(TRIALS):
    birthdays = []
    #23명이 모였을 때, 생일이 같다면 same_birthdays +=1
    for i in range(23):
        birthday = random.randint(1,365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)
print(f'{same_birthdays / TRIALS * 100}%')