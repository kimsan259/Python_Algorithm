# 자연수 n이 입력되면 1부터 n까지의 소수의 개수를 출력하는 프로그램

n = int(input())
ch = [0] * (n+1)
cnt = 0 # cnt는 소수의 개수
for i in range(2, n+1): # n까지 도려면 n+1
    if ch[i] == 0:
        cnt +=1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)
