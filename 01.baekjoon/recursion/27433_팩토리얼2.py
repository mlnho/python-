# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 20)이 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

# cnt = 0

import sys
def recursion(n):
    # global cnt
    # cnt += 1
    if n < 2:
        return 1
    return recursion(n-1) * n


# num = int(input())
num = int(sys.stdin.readline())
# cnt=0
print(recursion(num))
# print(cnt)