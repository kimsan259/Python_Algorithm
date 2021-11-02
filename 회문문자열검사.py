# (탐색&시뮬) 회문 문자열 검사
# N개의 문자열을 입력받아 앞에서 읽을때나 뒤에서 읽을때나 같은경우면 yes, 아니면 no, 단 대소문자 구별 x
# 2
# level / #1 YES
# moon  / #2 NO
import sys
n=int(input())
for i in range(n):
    s = input()
    s = s.upper()
 #   size = len(s)
 #  for j in range(size//2):
 #       if s[j]!=s[-1-j]:
 #           print("#%d NO" %(i+1))
 #           break
 #   else:
 #       print("#%d YES" % (i+1)) """    
    if s==s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
    