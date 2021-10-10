# N 명의 수학점수 중 평균을 구하고, N 명 중 가장 평균에 가장 가까운 학생은 몇번째인지 출력,
# 점수가 높고 번호가 빠른게 답
# 입럭 : 10
# 입력(2) : 65 73 66 87 92 67 55 71 75 80
# 출력 : 74
# 출력(2) : 9
import sys

n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n) 
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave,res)