# 문자와 숫자열이 섞여있는 문자열이 주어지면 숫자만 추출하여 자연수와 그 자연수의 약수 출력
# g0en2Ts8eSoft/28

import sys
s=input()
res=0
for x in s:
    print(x, end=' ') # 한칸씩 띄어서 s출력
    if x.isdecimal(): # 0~9까지만 출력
        res = res*10 + int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt+=1
print(cnt)

