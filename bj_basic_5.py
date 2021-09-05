#1
from sys import stdin

a = int(stdin.readline())
b = list(map(int, stdin.readline().split()))

b_min = b[0]
b_max = b[0]

for i in b:
    if i < b_min:
        b_min = i
    if i > b_max:
        b_max = i

print(b_min, b_max, end = ' ')

#1-1
from sys import stdin

a = int(stdin.readline())
b = list(map(int, stdin.readline().split()))

print(min(b), max(b), end=' ')


#2
from sys import stdin

num = []

for i in range(9):
    num.append(int(stdin.readline()))


print(max(num))
print(num.index(max(num))+1)


#3
from sys import stdin

a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())

mul = list(str(a * b * c)) # 문자를 세거나 위치를 알아 내는데에는 list가 딱인듯?

for i in range(10): # 0~9까지의 개수를 찾기 위해서
    print(mul.count(str(i))) # 문자열을 맞춰주는 것이 중요하다.


#4
from sys import stdin

arr = []

for i in range(10):
    n = int(stdin.readline())
    b = n % 42
    arr.append(b)
arr = set(arr) # 중복의 여부 판단은, 집합을 통해서 하면 간단.
print(len(arr))


#5

from sys import stdin

n = int(stdin.readline())
test_score = list(map(int, stdin.readline().split()))

max_t_s = max(test_score)
new_score = []

for i in test_score:
    new_score.append(i / max_t_s * 100)

t = sum(new_score) / n

print(t)


#6
# 런타임 에러
from sys import stdin

n = int(stdin.readline())

for i in range(n):
    a = int(stdin.readline())
    score = 0
    sumScore = 0
    for j in a :
        if j == 'O':
            score += 1
        else:
            score = 0 #score을 0으로 초기화 해주는 과정
        sumScore += score
    print(sumScore)


#6-1
N = int(input())

for i in range(N):
    a = input()
    score = 0
    sumScore = 0
    for j in a:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)
