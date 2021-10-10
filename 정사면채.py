# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력
# 입력은 N과 M이 주어진다. (4 6) , 출력 (5 6 7)
import sys
sys.stdin = open("input.txt","r")
n , m = map(int,input().split())
max = -2147000
cnt = [0] * (n+m+3)
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
for i in range(n+m+1):
    if cnt[i]>max:
        max = cnt[i]
for i in range(n+m+1):
    if cnt[i] == max:
        print(i , end= ' ')
